
import pika
import uuid

class FibonacciRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'
        ))

        self.channel = self.connection.channel()
        #生成一个随机queue
        result = self.channel.queue_declare('',exclusive= True)

        self.callback_queue = result.method.queue
        #从随机queue里获取返回值
        self.channel.basic_consume(self.callback_queue,
                                   self.on_response,#回调函数
                                   False)

    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        #客户端发送消息到rpc_queue，服务器端获取
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties = pika.BasicProperties(
                                       reply_to= self.callback_queue,#給sever指定返回值发送到queue
                                       correlation_id = self.corr_id,
                                   ),
                                   body=str(n))

        while self.response is None:
            #客户端还未收到返回值
            self.connection.process_data_events()
        return int(self.response)
fibonacci_rpc = FibonacciRpcClient()
print("[x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print("[.] Got %r" %response)