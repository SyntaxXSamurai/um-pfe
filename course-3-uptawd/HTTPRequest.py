import socket 

# Connecting to socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Getting data from the server
# Only part to change is the http link within the GET request
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n\'.encode()
mysock.send(cmd)

# User recieves data and prints/displays and formats for the user
# '512' in the recv() function refers to characters 
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()