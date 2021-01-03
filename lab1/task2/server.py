import socket
import json
import math

def welcome_message():
  return bytes('Available Options :-\na. Pythagorean theorem\nb. Solving a quadratic equation.\nc. Search for the area of ​​the trapezoid.\nd. Search for the area of ​​a parallelogram.', 'utf-8')

def Pythagorean_theorem(b, p):
  h = b**2 + p**2
  return math.sqrt(h)

def server_program():
  # get hostname and initiate port no. above 1024
  host = socket.gethostname()
  port = 5000

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((host, port))

  # configure how many client the server can listen simultaneously
  server_socket.listen(5)

  while True:
    conn, addr = server_socket.accept() # accept new connection
    print(f'Connection from {addr} has been established!')

    msg = welcome_message()
    conn.send(msg)
    option = json.loads(conn.recv(1024))
    op = option['op']
    if op == 'a':
      base = option['params']['base']
      perpendicular = option['params']['perpendicular']
      ans = Pythagorean_theorem(base, perpendicular)
      conn.send(bytes(f'Answer: hypotenuse - {round(ans, 2)}', 'utf-8'))

if __name__ == '__main__':
  server_program()