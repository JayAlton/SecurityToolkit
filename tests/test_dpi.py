import socket
import time
import threading

# Loopback interface for local testing
TARGET_IP = "127.0.0.1"

# Ports associated with known suspicious behavior
SUSPICIOUS_PORTS = [
        4444, 1337, 31337, 23, 2323, 666, 12345, 1433, 3389
]

# Malicious payloads that match SUSPICIOUS_PATTERNS in rules.py
SUSPICIOUS_PAYLOADS = [
        b"bash -i", b"/bin/sh", b"GET /shell", b"passwd", b"root:"
]

def send_payload(port, payload):
    """Send a TCP packet with suspicious payload to a specified port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((TARGET_IP, port))
            sock.sendall(payload)
            print(f"[TEST] Sent suspicious payload to {TARGET_IP}:{port}")
    except (ConnectionRefusedError, TimeoutError):
        print(f"[WARN] Connection refused or timed out on port {port} (still valid for DPI)")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

def test_dpi():
    """Run all suspicious port and payload combinations against DPI."""
    print("[*] Starting Deep Packet Inspection test...")
    for port in SUSPICIOUS_PORTS:
        for payload in SUSPICIOUS_PAYLOADS:
            threading.Thread(target=send_payload, args=(port, payload)).start()
            time.sleep(0.2) # delay to prevent the stack being overwhelmed

if __name__ == "__main__":
    test_dpi()
