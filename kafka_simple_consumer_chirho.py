#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import sys

import kafka
import argparse


def run_kafka_simple_listener_chirho(args_chirho: argparse.ArgumentParser):
    # Use a breakpoint in the code line below to debug your script.
    consumer_chirho = kafka.KafkaConsumer(
        args_chirho.topic_chirho,
        bootstrap_servers=args_chirho.server_chirho,
        group_id=args_chirho.group_id_chirho,
        client_id=args_chirho.client_id_chirho)

    for message_chirho in consumer_chirho:
        str_value_chirho = message_chirho.value.decode('utf-8')
        print(str_value_chirho)


def argparse_chirho():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic_chirho', type=str, default='tmp1_chirho')
    parser.add_argument('--server_chirho', type=str, help='server_ip:port', default='localhost:9092')
    parser.add_argument('--group_id_chirho', type=str, default=None)
    parser.add_argument('--client_id_chirho', type=str, default=None)

    args = parser.parse_args()
    return args


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args_chirho = argparse_chirho()
    print("Initializing consumer... Hallelujah!", file=sys.stderr)
    run_kafka_simple_listener_chirho(args_chirho)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
