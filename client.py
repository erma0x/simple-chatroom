import socket
import threading
from colorama import init, Fore, Style
import sys

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 60551)

# Connect to the server
client_socket.connect(server_address)

init()

if len(sys.argv) > 1:
    nickname = sys.argv[1]

else:
    nickname='unknown'

def receive_messages():
    while True:
        # Receive message from the server
        message = client_socket.recv(1024).decode('utf-8')
        
        # Print the received message
        print(Fore.YELLOW + message + Style.RESET_ALL)

# Start a new thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input(f'--[ {nickname} ]-> ')
    client_socket.send((nickname+' > '+message).encode('utf-8'))
    if message == 'exit':
        break

# Close the connection
client_socket.close()
