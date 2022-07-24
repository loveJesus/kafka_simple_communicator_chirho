#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import sys

import kafka
import argparse


def run_kafka_simple_producer_chirho(args_chirho: argparse.ArgumentParser):
    # Use a breakpoint in the code line below to debug your script.
    producer_chirho = kafka.KafkaProducer(
        bootstrap_servers=args_chirho.servers_chirho)

    for line_chirho in sys.stdin:
        producer_chirho.send(
            args_chirho.topic_chirho,
            line_chirho.strip().encode('utf-8'))
        producer_chirho.flush()


def argparse_chirho():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic_chirho', type=str, default='tmp1_chirho')
    parser.add_argument('--servers_chirho', type=str, help='server_ip:port,server_ip:port', default='localhost:9092')

    args = parser.parse_args()
    return args


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args_chirho = argparse_chirho()
    print("Initializing producer... Hallelujah!", file=sys.stderr)
    run_kafka_simple_producer_chirho(args_chirho)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
