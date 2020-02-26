

import socket,os

server = socket.socket()
server.bind(('localhost',9999))

server.listen()

while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令：",data)

        cmd_res = os.popen(data.decode()).read()#接受字符串，执行结果也是字符串
        print("before send", len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        conn.send(str(len(cmd_res.encode())).encode("utf-8")) #整数不能encode，所以转成字符串
        conn.send(cmd_res.encode("utf-8")) #没有全部发给客户端的会放在缓冲区，下次发自动发缓冲区里的数据
        print("send done")
server.close()