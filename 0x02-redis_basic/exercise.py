#!/usr/bin/env python3
"""Defines a class Cache."""
import uuid
import redis
from typing import Union


class Cache:
    """Handles caching."""

    def __init__(self):
        """Intanciates a new Cache."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates random key and store the arg data in it."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
