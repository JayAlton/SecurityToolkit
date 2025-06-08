# alert function
def alert(proto, src, sport, dst, dport, reasons):
    # Create a single string for alert reasons
    reason_str = ", ".join(reasons)
    print(f"ALERT [{proto}] {src}:{sport} -> {dst}:{dport} --- {reason_str}")
