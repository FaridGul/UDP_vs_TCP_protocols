import socket
import time

def traffic_generator(protocol="TCP", host="127.0.0.1", port=12345, num_messages=10, delay=0.5, log_file="results.txt"):
    results = []  # List to store traffic results

    try:
        # Initialize socket
        if protocol == "TCP":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
        elif protocol == "UDP":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print("Invalid protocol! Use 'TCP' or 'UDP'.")
            return

        print(f"Traffic generator running with {protocol} protocol...")

        for i in range(1, num_messages + 1):
            message = f"Message {i}"
            try:
                start_time = time.time()  # Record time before sending
                if protocol == "TCP":
                    client_socket.sendall(message.encode())
                    response = client_socket.recv(1024).decode()
                elif protocol == "UDP":
                    client_socket.sendto(message.encode(), (host, port))
                    response, _ = client_socket.recvfrom(1024)

                latency = time.time() - start_time  # Calculate latency
                results.append((message, response, "Success", latency))
                print(f"Sent: {message} | Received: {response} | Latency: {latency:.3f}s")
            except Exception as e:
                results.append((message, None, f"Failed: {str(e)}", None))
                print(f"Sent: {message} | Error: {str(e)}")
                break  # Stop sending messages if an error occurs

            time.sleep(delay)

    except Exception as e:
        print(f"Error establishing {protocol} connection: {str(e)}")
    finally:
        if protocol == "TCP":
            try:
                client_socket.close()
            except:
                pass

    # Save results to file
    with open(log_file, "a") as file:
        file.write(f"\n--- Traffic Results for {protocol} ---\n")
        for message, response, status, latency in results:
            file.write(f"Message: {message} | Response: {response} | Status: {status} | Latency: {latency}\n")

    print(f"\nResults saved to {log_file}")
    return results


if __name__ == "__main__":
    protocols = ["TCP", "UDP"]
    log_file = "results.txt"

    # Clear the log file before starting
    with open(log_file, "w") as file:
        file.write("TCP vs UDP Comparison Results\n")

    for protocol in protocols:
        print(f"\nRunning traffic generator for {protocol}...")
        traffic_generator(protocol=protocol, log_file=log_file)