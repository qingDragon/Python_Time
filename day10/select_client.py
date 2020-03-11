
import socket
import sys

messages = [
    b'This is the message.',
    b'It will be send',
    b'in the parts.',
]

server_address = ('10.211.55.6',9998)

socks = [socket.socket(socket.AF_INET,socket.SOCK_STREAM) for i in range(1000)]

print('connect to %s port %s' %server_address)

for s in socks:
    s.connect(server_address)

for message in messages:
    for s in socks:
        print('%s sending "%s"' % (s.getsockname(),message))
        s.send(message)

    for s in socks:
        data = s.recv(1024)
        print('%s received "%s' % (s.getsockname(),data))
        if not data:
            print(sys.stderr,'closing socket',s.getsockname())