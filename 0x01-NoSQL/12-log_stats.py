#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    collection = client.logs.nginx

    n_logs = collection.count_documents({})
    print(f"{n_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        total = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {total}")

    status_check = collection.count_documents({"methods": "GET", "path": "./status"})

    print(f"{status_check} status check")
