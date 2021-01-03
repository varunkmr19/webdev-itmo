import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))
s.send(bytes('Hello, server', 'utf-8'))
msg = s.recv(1024)
print(msg.decode('utf-8'))
s.close()