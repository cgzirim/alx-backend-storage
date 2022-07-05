#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient()
    db = client.logs

    display = """
    {} logs
    Methods:
        method GET: {}
        method POST: {}
        method PUT: {}
        method PATCH: {}
        method DELETE: {}
    {} status check
                """.format(
        db.ngix.find().count,
        db.nginx.find(db.nginx.find({"method": "GET"}).count()),
        db.nginx.find(db.nginx.find({"method": "POST"}).count()),
        db.nginx.find(db.nginx.find({"method": "PUT"}).count()),
        db.nginx.find(db.nginx.find({"method": "PATHC"}).count()),
        db.nginx.find(db.nginx.find({"method": "DELETE"}).count()),
        db.nginx.find(db.nginx.find({"method": "GET", "path": "/status"}).count()),
    )

    print(display)
