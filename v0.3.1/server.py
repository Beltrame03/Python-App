import os
import socket
import json

def dump(message):
    #items = {"message":"welcome"}
    #with open('messages.json', 'w') as f:
    #json.dump({items}, f)
    l = 0

    items = {}
    f = open('messages.json')
    Files = json.load(f)
    x = 1
    while (x == 1):
        try:
            print(Files[str(l)])
            l += 1
        except:
            x = 0

    for i in range(l):
        items[str(i)] = Files[str(i)]


    items[str(l)] = {"message": message}


    for m in range(len(items)):
        if(m > l):
            break
        else:
            print(items[str(m)])



    with open('messages.json', 'w') as f:
        json.dump(items, f)


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
    dump(data.decode())
    if data == "exit":
        break
s.close()
os._exit(0)

