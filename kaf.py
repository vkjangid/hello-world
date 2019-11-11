from kafka import KafkaProducer

def run(self):
    producer = KafkaProducer(zookeeper='34.93.217.34:2181')
    future = producer.send('test1', b'hello world')

run()
