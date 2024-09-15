from http import client
import socket as sk
import threading

class TCPClient:
    def __init__(self, host, port, buffer_size=1024):
        self.host = host
        self.port = port
        self.sock = sk.socket(sk.AF_INET6, sk.SOCK_STREAM)
        self.sock.connect((host, port))
        self.buf_size = buffer_size

    def handle_client(self):
        self.sock.send(("alias:"+input("Enter alias >>> ")).encode())
        data = self.sock.recv(self.buf_size).decode()
        print(data)
        while True:
            msg = input("Enter message >>> ")
            if msg == "exit":
                self.sock.send(msg.encode())
                break
            self.sock.send(msg.encode())
            # data = self.sock.recv(self.buf_size).decode()
            # print(data)

    def close(self):
        self.sock.close()

if __name__ == "__main__":
    client = TCPClient("localhost", 12345)
    try:
        client.handle_client()
    finally:
        client.close()