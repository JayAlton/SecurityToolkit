import argparse

def main():
    parser = argparse.ArgumentParser(description="Python Security Automation Toolkit")
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('scan', help='Run port scanner')
    subparsers.add_parser('hash', help='Run file integrity checker')
    subparsers.add_parser('logs', help='Parse logs')
    subparsers.add_parser('subenum', help='Enumerate subdomains')

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
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
