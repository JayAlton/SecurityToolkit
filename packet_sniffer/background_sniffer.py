# background_sniffer.py
from multiprocessing import Process
from sniffer import run

if __name__ == "__main__":
    p = Process(target=run, kwargs={"forever": True, "alert_email": ""})
    p.start()
    print(f"Sniffer started in background with PID {p.pid}")
