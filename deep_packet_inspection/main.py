# Import required module
from .engine import start_sniffer

# Define function
def start_dpi():
    # Print to console for status
    print("Deep Packet Inspection started...")
    start_sniffer()
