#Work Queues
#这种模式下，RabbitMQ会默认把p发的消息一次分发给各个消费者，跟负载均衡差不多

import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

#声明queue
channel.queue_declare(queue='task_queue_1',
                      #消息持久化，保存在queue里的消息不会丢失
                      durable=True)

message = ''.join(sys.argv[1:]) or "HelloWorld! %s"%time.time()
channel.basic_publish(
    exchange='',
    routing_key='task_queue_1',
    body=message,
    # make message persistent 使消息不会丢失
    properties=pika.BasicProperties(delivery_mode=2))
print('[x] sent %r' %message)
connection.close()