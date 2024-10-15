import socket
import ipaddress
import threading
import json
import argparse
from concurrent.futures import ThreadPoolExecutor

def ping_ip(ip, ports):
    active_ports = []
    for port in ports:
        try:
            with socket.create_connection((str(ip), port), timeout=1):
                active_ports.append(port)
        except (socket.timeout, OSError):
            pass  # If it fails, do nothing
    return str(ip), active_ports

def scan_ips(network, ports, max_threads):
    results = {}
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_ip = {executor.submit(ping_ip, ip, ports): ip for ip in ipaddress.IPv4Network(network)}
        for future in future_to_ip:
            ip, active_ports = future.result()
            if active_ports:
                results[ip] = active_ports
                print(f"{ip} is active on ports: {active_ports}")
    return results

def save_results(results, filename):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP Scanner")
    parser.add_argument("network", help="Network range in CIDR notation (e.g., 192.168.1.0/24)")
    parser.add_argument("--ports", nargs='+', type=int, default=[80], help="Ports to scan (default: 80)")
    parser.add_argument("--threads", type=int, default=100, help="Number of concurrent threads (default: 100)")
    parser.add_argument("--output", help="File to save results (in JSON format)")

    args = parser.parse_args()
    
    results = scan_ips(args.network, args.ports, args.threads)

    if args.output:
        save_results(results, args.output)
