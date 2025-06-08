# Suspicious ports often used by malware, backdoors, etc.
SUSPICIOUS_PORTS = {4444, 1337, 31337, 23, 2323, 666, 12345, 1433, 3389}

# Known malicious payload snippets to detect
SUSPICIOUS_PATTERNS = [
        b"bash -i", b"/bin/sh", b"GET /shell", b"passwd", b"root:"
]
