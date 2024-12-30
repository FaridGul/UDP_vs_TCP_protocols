import socket

def tcp_client():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to TCP Server {host}:{port}")

    while True:
        message = input("You: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Server: {data.decode()}")

if __name__ == "__main__":
    tcp_client()