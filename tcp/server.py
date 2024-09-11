import socket as sk

class TCPServer:
    def __init__(self, host, port, num_connections=1, buffer_size=1024):
        self.host = host
        self.port = port
        self.sock = sk.socket(sk.AF_INET6, sk.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(num_connections)
        self.buf_size = buffer_size

    def handle_client(self, conn):
        data = conn.recv(self.buf_size)
        print("Received:", data)
        conn.sendall(data)
        conn.close()

    def run(self):
        print("Server is running...")
        while True:
            conn, addr = self.sock.accept()
            print(f"Connected by {addr}")
            self.handle_client(conn)

    def close(self):
        self.sock.close()

if __name__ == "__main__":
    server = TCPServer("localhost", 12345, num_connections=5)
    try:
        server.run()
    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        server.close()