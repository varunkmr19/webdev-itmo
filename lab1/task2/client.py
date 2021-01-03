import socket
import json

def client_program():
  host = socket.gethostname()
  port = 5000

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((host, port))

  while True:
    data = client_socket.recv(1024)
    print(data.decode('utf-8'))
    option = input('-> ')
    if option == 'a':
      # get base and perpendicular
      base = float(input('base -> '))
      perpendicular = float(input('perpendicular -> '))
      op = {
        "op": option,
        "params": {"base": base, "perpendicular": perpendicular}
        }
      client_socket.sendall(str.encode(json.dumps(op)))

if __name__ == '__main__':
  client_program()