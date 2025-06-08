import socket
import time

# Define the target and suspicious ports
target_ip = "127.0.0.1" # Loopback so the sniffer picks it up

# List of known suspicous ports commonly used
suspicious_ports = [4444, # Metasploit reverse shell
                    1337, # "leet" port, ofetn used for CTFs and hacks
                    31337, # Back Orifice, elite port
                    12345, # NetBus
                    27374, # Sub7
                    666, # Doom backdoor
                    2323, # Alt Telnet
]

# Function to open a TCP connection and send a test message to the specified port
def send_to_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1) # Set timeout so we don't hang on closed ports
            s.connect((target_ip, port)) # Try to connect to the target port
            s.sendall(b"TESTING SUSPICIOUS PORT\n") # send dummy payload
            print(f"Send data to port {port}")
    except ConnectionRefusedError:
        # Port is closed but the packet still reaches the sniffer
        print(f"Port {port} refused the connection (still triggers sniffer)")
    except Exception as e:
        # Catch all other unexpected errors
        print(f"Error on {port}: {e}")

if __name__ == "__main__":
    print("Starting suspicious traffic test...")
    for port in suspicious_ports:
        send_to_port(port)
        time.sleep(0.5) # Delay to avoid packet drops
