import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel() #声明一个管道

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

print("[x] send 'Hello World!'")
connection.close()