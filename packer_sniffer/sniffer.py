from scapy.all import sniff

def run():
    print("Sniffing 10 packets...")
    sniff(count=10, prn=lamba x: x.summary())

