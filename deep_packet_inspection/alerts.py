from .logger import log_alert

def alert(proto, src, sport, dst, dport, reasons):
    """
    Displays and logs an alert with packet details.
    """
    reason_str=", ".join(reasons)
    message = f"[ALERT] {proto} {src}:{sport} -> {dst}:{dport} | {reason_str}"
    print(message)
    log_alert(message)
