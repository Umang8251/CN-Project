#This is the working server side file
#import time
import socket
import sys
import os
import ssl

TCP_SERVER_HOST ='192.168.74.78'

# Server's SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="domainserver.crt", keyfile="private.key")

# TCP socket creation
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initialize the host
host = socket.gethostname()

# Initialize the port
port = 8080

# Bind the socket with port and host
server_socket.bind(('', port))

print("TCP Server is listening...")
server_socket.listen()

# Accept incoming connections
connection, address = server_socket.accept()
print(f"Connection established with {address}")

# Wrap the connection with SSL
connection = context.wrap_socket(connection, server_side=True)
msg_to_client="This is a test message to indicate that the SSL is established"
connection.sendall(msg_to_client.encode())
#connection.close()
#server_socket.close()

#tcp_server_socket, addr
#tcp_connection, address = server_socket.accept()

while True:
    print("\nAvailable commands: file, audio, video, delete, open")
    # take command as input
    command = input("Enter Command (type 'exit' to quit): ")

    # Send the command to the client
    connection.send(command.encode("utf-8"))
    # Check if the command is to exit
    if command.lower() == 'exit':
        print("Exiting...")
        break

    # Receive confirmation
    data = connection.recv(1024)

    if data:
        print("Command received and executed successfully.")

# Close connection
connection.close()


'''
1.Coloroma
2.multithreading
3.don't hardcode commands
4.multiple devices - use platform library
5.get ip addr dynamically on client side
6. more applications'''

