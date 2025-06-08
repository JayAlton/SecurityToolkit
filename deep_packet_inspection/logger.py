from datetime import datetime

# Log packet inspections
def log_packet(proto, src, sport, dst, dport, payload):
    # Format timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create log line
    line = f"[{timestamp}] {proto} {src}:{sport} -> {dst}:{dport}"
    # Print log to console
    print(line)
    # Future: write to rotating file log
