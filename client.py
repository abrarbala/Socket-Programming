import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.1"  
port = 1900  
client_socket.connect((host, port))
message = client_socket.recv(1024).decode('utf-8')
print("Message from server:", message)
client_socket.close()
