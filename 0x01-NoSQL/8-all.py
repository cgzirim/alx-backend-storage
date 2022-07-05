#!/usr/bin/env python3
"""Defines the function list_all()."""
import pymongo
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lsts all documents in the given collection."""
    return mongo_collection.find()
