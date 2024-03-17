#This is the final working slave
#import time
import socket
import sys
import os
import ssl


# TCP socket creation
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ssl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initialize the host
host = "192.168.74.78"
host1 = "10.0.2.15"

# Initialize the port
port = 8080

print("Connected to Server.")

# Client's SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
#context.load_verify_locations(cafile="server.crt")

# Wrap the connection with SSL
client_socket= context.wrap_socket(client_socket,server_hostname=host)
context.check_hostname= False
context.verify_mode=ssl.CERT_NONE

client_socket.bind((host1,port))
client_socket.connect((host, port))

data = client_socket.recv(1024)
print("Received from ssl",data.decode())


#client_socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Loop to receive and execute commands multiple times
while True:
    # receive the command from the master program
    command = client_socket.recv(1024).decode().strip()

    # match the command and execute it on the slave system
    if command == "open":
        print("Command is :", command)
        client_socket.send("Command received".encode())
        os.system('ls')
    elif command == "file":
        print("Command is :", command)
        client_socket.send("Command received".encode())
        os.system('gedit Test4.c')
    elif command == "audio":
        print("Command is :", command)
        client_socket.send("Command received".encode())
        os.system('play Test2.mp3')
    elif command == "video":
        print("Command is :", command)
        client_socket.send("Command received".encode())
        os.system('mplayer Test3.mp4')
    elif command == "delete":
        print("Command is :", command)
        client_socket.send("Command received".encode())
        os.system('rm Test1.txt')
    elif command == "exit":
    
        print("Exiting....")
        break;

# Close connection
client_socket.close()
