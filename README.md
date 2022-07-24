# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# John 3:16 (NKJV)
## A simple Kafka communicator, to pipe to or from bash, for example:

```shell
./kafka_simple_consumer_chirho.py --servers_chirho 127.0.0.1:9092 --topic_chirho tmp1_chirho | while read line_chirho; do my_command_chirho.sh $line_chirho; done

my_other_command_chirho.sh | ./kafka_simple_producer_chirho --servers_chirho 127.0.0.1:9092 --topic_chirho tmp1_chirho 
```


