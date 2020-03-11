import socket

client = socket.socket()
client.connect(('10.211.55.6',9998))

while True:
    msg = input(">>:").strip() # 不能发空内容
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8")) #发送的数据类型必须是bytes
    data = client.recv(1024)
    print("recv:",data.decode())
client.close()
