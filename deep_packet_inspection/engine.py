from scapy.all import sniff
from .analyzer import analyze_packet

# Sniff IP packets and send each to analyzer
def start_sniffer():
    sniff(filter="ip", prn=analyze_packet, store=False)
