

import socket,os,time

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
        #先发命令大小，再发数据，可能出现粘包，两次发送数据一起
        conn.send(str(len(cmd_res.encode())).encode("utf-8")) #整数不能encode，所以转成字符串
        #time.sleep(0.5) #将两条命令隔开
        client_ack = conn.recv(1024) #wait client to confirm 解决粘包的小方法
        print("client_ack:",client_ack.decode())
        conn.send(cmd_res.encode("utf-8")) #没有全部发给客户端的会放在缓冲区，下次发自动发缓冲区里的数据
        print("send done")
server.close()

