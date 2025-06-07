import smtplib
from email.mime.text import MIMEText
from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import defaultdict
from datetime import datetime

# Sus ports to watch out for
SUSPICIOUS_PORTS = {
        21, # FTP
        23, # Telnet
        69, # TFTP
        135, # Windows RPC
        445, # SMB
        666, # Doom backdoor
        31337, # Back Orifice, Elite port
        4444, # Metasploit default reverse shells
        12345, # Netbus
        27374, # Sub7
        2323, # Alternative telnet
        1337, # Meme hacker tools
        1433, # MSSQL (often targeted)
        3306, # MySQL (brute-forced often)
        3389, # RDP (brute-force, ransomware vector)
        5900, # VNC (often exposed)
        8080, # Proxies/web shells
}

# Packet tracing
packet_counts = defaultdict(int)
captured_packets = []

# Function that will send email alert if a suspicious port is detected
def send_email_alert(to_email, alert_msg):
    from_email = ""
    password = "your-app-password"
    msg = MIMEText(alert_msg)
    msg['Subject'] = "ALERT: Suspicious Port Activity Detected"
    msg['From'] = from_email
    msg['To']

    try: 
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)
            print(f"Alert sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function that will do analysis on each captured packet
def analyze_packet(packet, alert_email=None):
    if IP in packet:
        proto = None
        src = packet[IP].src
        dst = packet[IP].dst

        # Determine protocol and port info
        if TCP in packet:
            proto = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            proto = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        elif ICMP in packet:
            proto = "ICMP"
            sport = "-"
            dport = "-"
        else:
            proto = "OTHER"
            sport = "-"
            dport = "-"

        line = f"[{proto}] {src}:{sport} -> {dst}:{dport}"

        # Alert on suspicious ports
        if proto in ["TCP", "UDP"] and (sport in SUSPICIOUS_PORTS or dport in SUSPICIOUS_PORTS):
            line += " Suspicious port detected"
            if alert_email:
                send_email_alert(alert_email, line)

        print(line)
        packet_counts[proto] += 1
        captured_packets.append(line)

# Main sniffing function
def run(forever=False, alert_email=None):
    print("Starting packet capture (press Ctrl+C to stop)...\n")
    try:
        sniff(filter="ip", 
              prn=lambda pkt: analyze_packet(pkt, alert_email), 
              count=0 if forever else 50
        )
    except KeyboardInterrupt:
        print("\n Capture Interrupted.")

    # Summary of captured protocols
    print("\n Packet Summary: ")
    for proto, count in packet_counts.items():
        print(f" - {proto}: {count} packets")

    # Save to log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"packet_log_{timestamp}.txt", "w") as f:
        for entry in captured_packets:
            f.write(entry + "\n")
    print(f"\n Packet log saved to packet_log_{timestamp}.txt")

