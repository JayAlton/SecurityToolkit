from .rules import SUSPICIOUS_PORTS, SUSPICIOUS_PATTERNS
from .alerts import alert

# Define function that analyzes packets
def analyze_packet(pkt):
    """
    Analyzes an incoming packet and triggers alerts if it matches suspicious criteria
    """
    # Check if packet contains an IP layer
    if pkt.haslayer("IP"):
        # Extract IP fields
        ip = pkt["IP"]
        src = ip.src
        dst = ip.dst
        proto = pkt.lastlayer().name
        payload = bytes(pkt.payload)

        # Extract source/destination ports if available
        sport = getattr(pkt, "sport", "-")
        dport = getattr(pkt, "dport", "-")

        reasons = []

        # Check for suspicious port usage
        if sport in SUSPICIOUS_PORTS or dport in SUSPICIOUS_PORTS:
            reasons.append("suspicious port")

        # Check for known suspicious payload patterns
        for pattern in SUSPICIOUS_PATTERNS:
            if pattern in payload:
                reasons.append(f"payload match: {pattern.decode(errors='ignore')}")

        # If any issues were found, trigger alert
        if reasons:
            print(f"Seen packet: {proto} {src}:{sport} -> {dst}:{dport}")
            alert(proto, src, sport, dst, dport, reasons)
