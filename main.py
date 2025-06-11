import argparse

def main():
    parser = argparse.ArgumentParser(description="Python Security Automation Toolkit")
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('scan', help='Run port scanner')
    subparsers.add_parser('hash', help='Run file integrity checker')
    subparsers.add_parser('logs', help='Parse logs')
    subparsers.add_parser('subenum', help='Enumerate subdomains')
    
    # Add options for the packet sniffer
    sniff_parser = subparsers.add_parser('sniff', help='Sniff packets')
    sniff_parser.add_argument('--forever', action='store_true', help='Run sniffer continuously')
    sniff_parser.add_argument('--alert', type=str, help='Send email alert to this address')

    # Deep Packet inspection
    subparsers.add_parser('dpi', help='Run Deep Packet Inspection sniffer')

    # Vulnerability scan
    subparsers.add_parser('vulnscan', help='Check for vulnerabilities')

    args = parser.parse_args()

    if args.command == 'scan':
        from portscanner.portscan import run
        run()
    elif args.command == 'hash':
        from file_integrity.integrity_checker import run
        run()
    elif args.command == 'logs':
        from log_parser.parse_logs import run
        run()
    elif args.command == 'subenum':
        from subdomain_enum.sub_enum import run
        run()
    elif args.command == 'sniff':
        from packet_sniffer.sniffer import run
        run(forever=args.forever, alert_email=args.alert)
    elif args.command == 'dpi':
        from deep_packet_inspection.dpi import start_dpi
        start_dpi()
    elif args.command == 'vulnscan':
        from vulnerability_scanner.vulnerscanner import run
        run()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
