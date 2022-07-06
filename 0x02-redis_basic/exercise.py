#!/usr/bin/env python3
"""Defines a class Cache."""
import uuid
import redis
from typing import Callable, Optional, Union


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

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Gets data from the cache."""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Gets a string from the cache"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Converts redis data to int."""
        data = self._redis.get(key)
        return int(data)
