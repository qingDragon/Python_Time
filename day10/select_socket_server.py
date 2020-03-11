
import select
import socket
import queue

server = socket.socket()
server.bind(("127.0.0.1",9999))
server.listen(1000)

server.setblocking(False) #设置为不阻塞

inputs = [server,]
outputs = []
con_dict = dict()
while True:
    readable, writeable, exceptionbal = select.select(inputs,outputs,inputs)
    print(readable,writeable,exceptionbal)

    for r in readable:
        if r is server:#代表来了一个新连接
            print("获得了一个新的连接")
            conn,addr = server.accept()
            inputs.append(conn)#新建立的连接还没发数据过来，要实现客户端发数据来时server能知道，就需要让select再监测这个连接
            con_dict[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            if data:
                print("收到来自[%s]的数据:" % r.getpeername()[0],data)
                con_dict[r].put(data)
                if r not in outputs:
                    outputs.append(r)
            else:
                print("客户端断开了",r)
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                del con_dict[r]
    for w in writeable:
        try:
            data = con_dict[w].get_nowait()
        except queue.Empty:
            print("client [%s]" %w.getpeername()[0],"queue is enpty..")
            outputs.remove(w)
        else:
            w.send(data.upper())
            outputs.remove(w)

    for e in exceptionbal:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        e.close()
        del con_dict[e]