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

## ⚙️ Installation and use with Python3

### 1. Clone the Repository
```bash
git clone https://github.com/JayAlton/SecurityToolkit.git
cd SecurityToolkit

### 2. Create Virtual Environment

Make sure python version is 3.11 to use this toolkit

python3 -m venv .venv

```Windows: 
.\.venv\Script\activate

```Linux:
.venv/source/activate

### 3. Install Requirements

pip install -r requirements.txt

Note: For packet sniffing you may need sudo

### 4. Run Main Function

python3 main.py
