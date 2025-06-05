import pyfiglet
import sys
import socket
from datetime import datetime

def run():
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)
    
    target_input = input("Enter hostname or IP to scan: ").strip()

    try:
        target = socket.gethostbyname(target_input)
    except socket.gaierror:
        print("X Hostname could not be resolved.")
        return

    print("-" * 50)
    print(f"Scanning Target: {target}")
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)

    try:
        for port in range(1, 1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port} is open")
    except KeyboardInterrupt:
        print("\n Exiting Program...")
    except socket.error:
        print("\n Server not responding")
        
