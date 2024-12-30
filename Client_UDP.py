import socket

def udp_client():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("You: ")
        client_socket.sendto(message.encode(), (host, port))
        data, _ = client_socket.recvfrom(1024)
        print(f"Server: {data.decode()}")

if __name__ == "__main__":
    udp_client()