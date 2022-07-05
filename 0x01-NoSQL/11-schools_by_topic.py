#!/usr/bin/env python3
"""Defines the funtion schools_by_topics."""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic."""
    return mongo_collection.find({"topic": topic})