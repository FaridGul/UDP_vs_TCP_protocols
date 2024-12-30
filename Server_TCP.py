import socket

def tcp_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"TCP Server is running on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Client: {data.decode()}")
        message = input("You: ")
        conn.sendall(message.encode())

    conn.close()

if __name__ == "__main__":
    tcp_server()