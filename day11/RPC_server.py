
import pika

import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
#创建管道
channel = connection.channel()
#创建队列
channel.queue_declare(queue='rpc_queue')

def fib(n):
    "斐波拉契数列"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def on_request(ch,method,props,body):
    "服务器的回调函数--收到客户端发的数据后自动调用，给客户端返回信息"
    n = int(body)
    print("[.]fib(%s)" %n)
    response = fib(n)
    #发送返回信息给客户端
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id = props.correlation_id),#客户端发数据来指定的校验id，连同返回数据一起发回给客户端，校验用
                     body=str(response))

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) #只能有一个未处理消息
#服务器从rpc_queue中获取客户端的请求，获取到后调用on——resquest回调函数给客户端指定queue发送返回数据
channel.basic_consume("rpc_queue",
                      on_request)
print("[x] Waiting RPC resquests")
channel.start_consuming()