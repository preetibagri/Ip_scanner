# Ip_scanner
Steps explained
# Imports:
socket: Provides low-level networking interfaces.
ipaddress: Used to create, manipulate, and validate IP addresses and networks.
threading: Supports threading to perform tasks concurrently.
json: For handling JSON data, such as saving results.
argparse: Facilitates command-line argument parsing.
ThreadPoolExecutor: Manages a pool of threads for concurrent execution.

# Function Definition: Defines the ping_ip function, which takes an IP address and a list of ports to scan.

# Active Ports List: Initializes an empty list to store ports that are open for the given IP.

# Port Loop: Iterates over each port provided in the ports list

# Socket Connection: Attempts to create a socket connection to the specified IP and port with a timeout of 1 second.

# Store Active Port: If the connection is successful, the port is added to the active_ports list.

# Exception Handling: If the connection times out or fails due to an operating system error, it catches the exception and does nothing.

# Return Statement: Returns a tuple containing the IP address and the list of active ports.

# Function Definition: Defines the scan_ips function, which scans a given network for active ports on specified IPs.

# Results Dictionary: Initializes an empty dictionary to store results of the scan.

# Thread Pool Executor: Creates a thread pool that allows a maximum number of concurrent threads defined by max_threads.

# Submit Tasks: Submits tasks to the executor for each IP in the specified network, storing the future (the result of the operation) along with the corresponding IP in a dictionary.

# Future Loop: Iterates over the submitted futures to retrieve results.

# Retrieve Result: Gets the result from each future, unpacking it into ip and active_ports.

# Check for Active Ports: If the active_ports list is not empty, it means the IP is active.

# Store Results: Adds the active ports for the IP to the results dictionary.

# Print Active Ports: Outputs the active IP and its open ports to the console.

# Return Statement: Returns the results dictionary containing all active IPs and their corresponding open ports.

# Function Definition: Defines the save_results function, which saves scan results to a specified file.

# Open File: Opens the specified file in write mode.

# Write JSON: Serializes the results dictionary to JSON format and writes it to the file with indentation for readability.

# Main Check: Ensures that the following code runs only if the script is executed directly.

# Argument Parser: Initializes the argument parser for handling command-line arguments.

# Network Argument: Adds a positional argument for the network range in CIDR notation.

# Ports Argument: Adds an optional argument for specifying ports to scan, accepting multiple integers with a default of port 80.

# Threads Argument: Adds an optional argument for specifying the maximum number of concurrent threads, defaulting to 100.

# Output File Argument: Adds an optional argument to specify a filename to save results in JSON format.

# Parse Arguments: Parses the command-line arguments and stores them in the args variable.

# Call Scan Function: Calls the scan_ips function with the provided network, ports, and thread count, storing the results.

# Save Results: If an output filename is provided, calls save_results to write the results to that file.

# How to Use the Script
python Ip_Scanner.py <network> [--ports PORTS [PORTS ...]] [--threads THREADS] [--output OUTPUT]

# Basic usage
python Ip_Scanner.py 192.168.1.0/24

# Specify Ports 
python Ip_Scanner.py 192.168.1.0/24 --ports 80 22

# Specify Number of Threads:
python Ip_Scanner.py 192.168.1.0/24 --threads 50

# Save results of file
python Ip_Scanner.py 192.168.1.0/24 --output results.json

# Complete Command Example
python Ip_Scanner.py 192.168.1.0/24 --ports 80 22 443 --threads 100 --output results.json
