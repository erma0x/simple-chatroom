import select
import socket
import sys

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the server socket to a specific address and port
server_address = ('localhost', 60551)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(10)

# List to keep track of connected clients
client_sockets = [server_socket]

print("Chatroom server started on {}:{}".format(*server_address))

while True:
    # Use select to monitor the sockets for I/O readiness
    readable, _, _ = select.select(client_sockets, [], [])

    for sock in readable:
        if sock is server_socket:
            # Accept new connection
            client_socket, client_address = server_socket.accept()
            client_sockets.append(client_socket)
            print("New client connected: {}".format(client_address))
        else:
            # Receive and broadcast messages
            data = sock.recv(1024)
            if data:
                message = data.decode().strip()
                print("Received message: {}".format(message))
                # Broadcast the message to all connected clients
                for client in client_sockets:
                    if client is not server_socket and client is not sock:
                        client.sendall(data)
            else:
                # Remove disconnected client
                client_sockets.remove(sock)
                sock.close()

