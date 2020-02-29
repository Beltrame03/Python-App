import socket

host = "localhost"
port = 45
buf = 1024
addr = (socket.gethostname(), 1234)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(5)
print ("Waiting to receive messages...")
while True:
    clientsocket, address = s.accept()
    data = clientsocket.recv(1024)
    print(data.decode())
    print(f"Connection from {address} has been establisehd")
    clientsocket.send(bytes("welcome",  "utf-8"))
    clientsocket.close()
