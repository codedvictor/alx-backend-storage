#!/usr/bin/env python3
"""
Advanced tasks with tools for request caching and tracking.
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
"""
redis instance module
"""


def data_cacher(method: Callable) -> Callable:
    """
    Caches the output of fetched data.
    """
    @wraps(method)
    def invoker(url) -> str:
        """
        The wrapper function for caching the output.
        """
        redis_store.incr(f'count:{url}')
        get_result = redis_store.get(f'result:{url}')
        if get_result:
            return get_result.decode('utf-8')
        get_result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, get_result)
        return get_result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Returns the content of a URL and tracking the request.
    """
    return requests.get(url).text
