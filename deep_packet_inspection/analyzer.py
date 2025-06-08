from rules import SUSPICOUS_PORTS, SUSPICIOUS_PATTERNS
from alerts import alert
from logger import log_packet

# Define function that analyzes packets
def analyze_packet(pkt):
    # Check if packet contains an IP layer
    if pkt.haslayer("IP"):
        # Extract IP fields
        ip = pkt["IP"]
        src - ip.src
        dst = ip.dst
        proto = pkt.lastlayer().name
        payload = bytes(pkt.payload)

        # Extract source/destination ports if available
        sport = pkt.sport if hasattr(pkt, "sport") else "-"
        dport = pkt.dport if hasattr(pkt, "dport") else "-"

        alert_flag = False
        reasons = []

        # Check for suspicious port usage
        if sport in SUSPICIOUS_PORTS or dport in SUSPICIOUS_PORTS:
            alert_flag = True
            reasons.append("suspicious port")

        # Check for known suspicious payload patterns
        for pattern in SUSPICIOUS_PATTERNS:
            if pattern in payload:
                alert_flag = True
                reasons.append(f"payload match: {pattern.decode(errors='ignore')}")

        # Log the packet details
        log_packet(proto, src, sport, dst, dport, payload)

        # If any issues were found, trigger alert
        if alert_flag:
            alert(proto, src, sport, dst, dport, reasons)
