#!/usr/bin/env python3
"""Defines a class Cache."""
import uuid
from typing import Union
import redis


class Cache:
    """Handles caching."""

    def __init__(self):
        """Intanciates a new Cache."""
        self._redis = redis.Redis()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Generates random key and store the arg data in it."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
