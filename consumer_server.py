from kafka import KafkaConsumer
#Simple consumer code print the produced data from "sfo.police.call.events" topic
consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=2000)

consumer.subscribe(['sfo.police.call.events'])
for message in consumer:
    print(message.value)
