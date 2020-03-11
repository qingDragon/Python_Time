
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# try:
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# except Exception as e:
#     print(e)
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print("[x] Received '%r' " %body)
channel.basic_consume('hello', callback , False )  #参数位置发生了改变，挂了很久

print('[*] Waiting for messages.To exit press CTRL+C')
channel.start_consuming()