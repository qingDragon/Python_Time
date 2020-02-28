

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                # if not self.data:
                #     print(self.client_address,"断开了")
                #     break
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST,PORT = "localhost",9999

    server = socketserver.ForkingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()