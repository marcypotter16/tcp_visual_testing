import socket as sk

class TCPServer:
    def __init__(self, host, port, num_connections=1, buffer_size=1024):
        self.host = host
        self.port = port
        self.sock = sk.socket(sk.AF_INET6, sk.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(num_connections)
        self.buf_size = buffer_size
        self.clients = {}

    def handle_client(self, conn):
        data = conn.recv(self.buf_size).decode("utf-8")
        print("Received:", data)
        if data == "exit":
            print(f"Client {conn.getpeername()} disconnected")
            conn.close()
            return
        if data.startswith("alias:"):
            alias = data.split(":")[1]
            self.clients[alias] = conn
            print(f"Alias set to {alias}")
            conn.sendall(f"{alias} connected to the lobby".encode("utf-8"))
        else:
            for client in self.clients.values():
                client.sendall(data.encode("utf-8"))
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