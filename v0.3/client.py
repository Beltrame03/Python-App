import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (socket.gethostname(), 1234)
s.connect(addr)
msg = "hay"
s.send(str.encode(msg))

