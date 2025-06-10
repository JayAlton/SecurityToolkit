# Suspicious ports often used by malware, backdoors, etc.
SUSPICIOUS_PORTS = {21, 69, 135, 445, 4444, 1337, 31337, 
                    23, 2323, 666, 12345, 27374, 1433, 3306, 5900, 8080, 3389}

# Known malicious payload snippets to detect
SUSPICIOUS_PATTERNS = [
        b"bash -i", 
        b"rm -rf /",
        b"curl http://",
        b"powershell",
        b"eval("
        b"nc -e"
        b"/bin/sh", 
        b"GET /shell", 
        b"passwd", 
        b"root:"
]
