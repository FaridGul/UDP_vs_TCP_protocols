import socket

def udp_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server is running on {host}:{port}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Client {addr}: {data.decode()}")
        message = input("You: ")
        server_socket.sendto(message.encode(), addr)

if __name__ == "__main__":
    udp_server()