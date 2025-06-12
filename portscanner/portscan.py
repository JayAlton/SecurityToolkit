import pyfiglet
import os
import argparse
import logging
import sys
import socket
from datetime import datetime

def run(log):
    if log:
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"logs/portscan_{timestamp}.log"
        logging.basicConfig(
                filename=log_file,
                level=logging.INFO,
                format="%(asctime)s - %(message)s"
        )
        logging.info("Started logging port scan...")

    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)
    
    target_input = input("Enter hostname or IP to scan: ").strip()

    try:
        target = socket.gethostbyname(target_input)
    except socket.gaierror:
        print("X Hostname could not be resolved.")
        if log: logging.error(f"Hostname resolution failed for: {target_input}")
        return

    print("-" * 50)
    print(f"Scanning Target: {target}")
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)
    if log: logging.info(f"Scanning target: {target}")

    try:
        for port in range(1, 1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    msg = f"Port {port} is open"
                    print(msg)
                    if log: logging.info(msg)
    except KeyboardInterrupt:
        print("\n Exiting Program...")
        if log: logging.warning("Scan interrupted by user.")
    except socket.error:
        print("\n Server not responding")
        if log: logging.error(f"Socket error:{e}")
