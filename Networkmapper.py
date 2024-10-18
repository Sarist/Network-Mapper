import nmap
import pyfiglet

# Simulated vulnerability database for common issues
vulnerability_db = {
    22: "Potential SSH misconfiguration (OpenSSH outdated version).",
    80: "HTTP server vulnerable to XSS (check headers).",
    443: "SSL/TTLS misconfiguration (weak ciphers or outdated SSL).",
    21: "FTP anonymous login enabled (check access restrictions)."
}

# Function to display the terminal header
def display_header():
    ascii_banner = pyfiglet.figlet_format("Network Mapper")
    print(ascii_banner)
    print(" " * 40 + "by Sarist")
    print("=" * 70)

# Function to simulate vulnerability scanning based on open ports
def vulnerability_scan(port):
    if port in vulnerability_db:
        return vulnerability_db[port]
    return "No known vulnerabilities found for this port."

# Function to scan a single IP for open ports
def scan_ip(ip):
    nm = nmap.PortScanner()
    print(f"Scanning IP: {ip}")
    nm.scan(ip, '1-1024')  # Scanning ports 1 to 1024

    if ip in nm.all_hosts():
        print(f"\nResults for {ip}:")
        for proto in nm[ip].all_protocols():
            ports = nm[ip][proto].keys()
            for port in ports:
                state = nm[ip][proto][port]['state']
                service = nm[ip][proto][port]['name']
                vulnerability = vulnerability_scan(port)
                print(f"Port {port} is {state} (Service: {service}) - {vulnerability}")
    else:
        print(f"No open ports found on {ip}")

# Function to scan a range of IPs
def scan_ip_range(start_ip, end_ip):
    start_segments = list(map(int, start_ip.split('.')))
    end_segments = list(map(int, end_ip.split('.')))

    for i in range(start_segments[3], end_segments[3] + 1):
        current_ip = f"{start_segments[0]}.{start_segments[1]}.{start_segments[2]}.{i}"
        scan_ip(current_ip)

if __name__ == "__main__":
    # Display the header
    display_header()
    
    # Select between single IP or IP range
    print("Choose the scan type:")
    print("1. Scan a Single IP")
    print("2. Scan a Range of IPs")
    
    scan_type = input("Enter your choice (1 or 2): ")

    if scan_type == "1":
        # Single IP scan
        single_ip = input("Enter the IP address to scan: ")
        scan_ip(single_ip)
    elif scan_type == "2":
        # IP range scan
        start_ip = input("Enter the starting IP: ")
        end_ip = input("Enter the ending IP: ")
        scan_ip_range(start_ip, end_ip)
    else:
        print("Invalid option selected. Please choose 1 or 2.")
