import socket

def run():
    domain = input("Enter domain to enumerate: ")
    subdomains = ["www", "mail", "ftp", "test"]
    for sub in subdomains:
        try:
            full = f"{sub}.{domain}"
            ip = socket.gethostbyname(full)
            print(f"{full} -> {ip}")
        except socket.gaierror:
            continue

