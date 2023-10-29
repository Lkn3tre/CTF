import socket

# Define the host and port to listen on
host = "0.0.0.0"  # Listens on all available network interfaces
port = 8080

# Create a socket and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"Listening on {host}:{port}")

while True:
    data, addr = server_socket.recvfrom(1024)  # Receive data from clients
    print(f"Received data from {addr}: {data.decode('utf-8')}")

server_socket.close()
