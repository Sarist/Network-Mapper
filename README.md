# Network Mapping and Vulnerability Scanning Tool

## Overview

This tool is designed for penetration testers and security professionals to map networks, identify open ports, and scan for common vulnerabilities. Built on **Kali Linux**, this command-line tool leverages Python's `nmap` library to scan IP ranges or individual IPs and detect potential vulnerabilities associated with specific ports.

### Features
- **Single IP or IP Range Scanning**: Choose between scanning a single IP or a range of IPs to get insights into network devices and services.
- **Open Port Detection**: Identifies open ports and associated services for each host on the network.
- **Vulnerability Scanning**: Includes a simulated vulnerability database that highlights common misconfigurations and security risks for identified ports.
- **Command-line Interface**: Easily run the tool from the command line with minimal setup on Kali Linux.
  
## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Requirements

This tool is developed on **Kali Linux** and requires the following dependencies:

- Python 3.x
- Nmap
- Pyfiglet (for the header display)

To install the required dependencies, run:

```bash
sudo apt update
sudo apt install nmap python3-pip
pip3 install python-nmap pyfiglet
```

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/network-mapper.git
cd network-mapper
```

Ensure all the dependencies listed above are installed. Then, you can directly run the script in your terminal.

## Usage

Run the tool using Python 3 from the command line:

```bash
python3 network_mapper.py
```

### Steps:
1. **Select Scan Type**: Upon running the script, you’ll be prompted to choose between scanning a **Single IP** or an **IP Range**.
2. **Enter IP/Range**: Based on your selection, input either a single IP address or a starting and ending IP range.
3. **View Results**: The tool will scan the provided IP(s) and display open ports, services, and any vulnerabilities associated with the detected ports.

### Example Usage

```bash
# Single IP scan
Enter your choice (1 or 2): 1
Enter the IP address to scan: 192.168.1.5

# Range of IPs scan
Enter your choice (1 or 2): 2
Enter the starting IP: 192.168.1.1
Enter the ending IP: 192.168.1.10
```

### Output

The scan results display each detected open port, its state, the associated service, and any known vulnerabilities, for example:

```
Port 22 is open (Service: ssh) - Potential SSH misconfiguration (OpenSSH outdated version).
Port 80 is open (Service: http) - HTTP server vulnerable to XSS (check headers).
Port 443 is open (Service: https) - SSL/TTLS misconfiguration (weak ciphers or outdated SSL).
```

## Features

- **Network Enumeration**: Scans up to 1024 common ports on each device within the specified IP range or single IP.
- **Vulnerability Database**: A built-in simulated vulnerability detection mechanism that identifies common security issues such as:
  - Outdated SSH services
  - HTTP servers vulnerable to cross-site scripting (XSS)
  - SSL/TLS misconfigurations
  - FTP services allowing anonymous login
- **Simple Interface**: Clean, ASCII art-enhanced command-line interface using Pyfiglet for an intuitive user experience.

## Customizing the Vulnerability Database

You can easily extend the vulnerability detection functionality by adding more vulnerabilities in the `vulnerability_db` dictionary located in the code:

```python
vulnerability_db = {
    22: "Potential SSH misconfiguration (OpenSSH outdated version).",
    80: "HTTP server vulnerable to XSS (check headers).",
    443: "SSL/TLS misconfiguration (weak ciphers or outdated SSL).",
    21: "FTP anonymous login enabled (check access restrictions)."
}
```

Feel free to add more ports and associated vulnerabilities to tailor the tool to your needs.

## Future Enhancements

- **Automated vulnerability scanning with CVE lookup**.
- **Integration with more comprehensive vulnerability databases**.
- **Addition of custom port ranges for scanning**.
- **Optional GUI frontend** to complement the command-line interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
