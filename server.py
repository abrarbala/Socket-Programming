import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.1" 
port = 1900  
server_socket.bind((host, port))
server_socket.listen(5) 
print("Server is listening on {}:{}".format(host, port))
while True:
    client_socket, address = server_socket.accept()
    print("Connection from", address)
    message = "Connection successful!"
    client_socket.send(message.encode('utf-8'))
    client_socket.close()

