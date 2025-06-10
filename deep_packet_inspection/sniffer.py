from scapy.all import sniff
from .analyzer import analyze_packet

# Currently sniffs packets on loopback address
# Future change this to default to loopback address 
def start_sniffer(interface="lo"):
    """
    Starts the packet sniffer on the specified interface.
    If no interface is given, listens on all interfaces.
    """
    try:
        print(f"[i] Sniffing on interface: {interface}")
        sniff(
                iface=interface,
                prn=analyze_packet, # callback for each packet
                store=False
        )
    except Exception as e:
        print(f"[!] Sniffer failed: {e}")
    except PermissionError:
        print("Run with sudo: packet sniffing requires root privileges.")

