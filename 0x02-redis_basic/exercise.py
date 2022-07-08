#!/usr/bin/env python3
"""Defines a class Cache."""
import uuid
import redis
from functools import wraps
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """Decorator to count number of times methods of Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper of decorator."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a method in
    the Cache class.
    """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper of decorator."""
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, method(self, *args))
        return method(self, *args, **kwargs)

    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls of a particular function."""
    key = method.__qualname__
    r_instance = method.__self__._redis
    times_called = r_instance.get(key).decode("utf-8")
    inputs = r_instance.lrange(key + ":inputs", 0, -1)
    outputs = r_instance.lrange(key + ":outputs", 0, -1)
    zipped = zip(inputs, outputs)

    print(f"{method.__qualname__} was called {times_called} times")
    for input, output in zipped:
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print(f"{method.__qualname__}(*{input}) -> {output}")


class Cache:
    """Handles caching."""

    def __init__(self):
        """Intanciates a new Cache."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        """Converts redis data to string."""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Converts redis data to int."""
        data = self._redis.get(key)
        return int(data)
