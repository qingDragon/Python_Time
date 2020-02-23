import os
import socket

server = socket.socket()
server.bind(('localhost',6969))

server.listen()
print("我要开始等电话了")
while True:
    conn,addr = server.accept()
    print(conn,addr)

    print("电话来了")
    while True:
        data = conn.recv(1024)
        print("recv:",data)
        if not data:
            print("client has lost...")
            break
        res = os.popen(data).read()
        conn.send(res)
server.close()