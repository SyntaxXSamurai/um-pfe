import socket 

# In-built support for TCP-Sockets in Python
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# First part of input is the host
# Second part of input is the port
mysock.connect(('data.pr4e.org', 80))