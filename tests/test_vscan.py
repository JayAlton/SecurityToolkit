import socket
import threading

FAKE_BANNER = b"220 OpenSSH 7.2p2 Ubuntu-4ubuntu2.8"

def start_fake_service(host="127.0.0.1", port=2222):
    def handler(client_socket):
        client_socket.send(FAKE_BANNER)
        client_socket.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[FAKE SERVICE] Listening on {host}:{port}")
    while True:
        client, _ = server.accept()
        threading.Thread(target=handler, args=(client,), daemon=True).start()

if __name__ == "__main__":
    start_fake_service()
