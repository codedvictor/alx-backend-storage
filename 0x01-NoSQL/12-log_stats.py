#!/usr/bin/env python3
"""
 a Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def print_request_logs(nginx_collection):
    """
    Prints stats about Nginx request logs.
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        request_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, request_count))
    checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(checks_count))


def run():
    """
    execute logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
