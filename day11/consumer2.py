
import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue_1',durable=True)

print('[*]Waiting for message. To exit press CRTL+C')

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    time.sleep(20)
    print("[x] Done")
    # print('method.delivery_tag',method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1) #告诉rabbitmq在这个消费当前消息还没处理完就不要再发新的
channel.basic_consume("task_queue_1", callback, False)

channel.start_consuming()