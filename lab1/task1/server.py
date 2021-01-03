import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5000))
s.listen(1)

conn, address = s.accept()
print(f'Connection from {address} has been established!')
while True:
  msg = conn.recv(1024)
  if not msg:
    break
  print(msg.decode('utf-8'))
  conn.send(bytes('Hello, client', 'utf-8'))
conn.close()