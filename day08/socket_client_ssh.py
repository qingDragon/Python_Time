

import socket
client = socket.socket()

client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024) #接受命令结果长度
    # cmd_res = client.recv(1024) #虽然写的1024，代表最多是1024，不一定每次都收满
    # print(cmd_res.decode())
    client.send("准备好接受了，loser可以发了".encode("utf-8"))
    print("命令结果长度：",cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()): #linux上发送数据长度的时候会默认加上数据
        data = client.recv(1024)
        received_size += len(data) #每次收到的有可能小于1024，所以必须用len判断
        # print(data.decode())
        received_data += data
        print(received_size)
    else:
        print("receive done",received_size)
        print(received_data.decode())
client.close()