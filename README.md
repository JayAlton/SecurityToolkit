# 🔐 SecurityToolkit – Python Security Automation Toolkit

A modular Python-based toolkit to automate common cybersecurity tasks like port scanning, log parsing, file integrity checking, and network sniffing. Built to showcase practical skills aligned with CompTIA Security+.

---

## 🚀 Features

| Module    | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| `scan`    | TCP port scanner with service detection and banner grabbing                |
| `hash`    | File integrity checker using SHA-256                                       |
| `logs`    | Log parser to detect suspicious events (e.g., failed logins)               |
| `subenum` | Subdomain enumeration using DNS brute-force                                |
| `sniff`   | Packet sniffer with suspicious port alerts and optional email notifications|
| `vscan`   | (Placeholder) Vulnerability scanner (planned integration with CVE APIs)    |

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/security-toolkit.git
cd security-toolkit

### 2. Install Requirements

pip install -r requirements.txt

Note: For packet sniffing you may need sudo


