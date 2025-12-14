from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}
    def wrapper(*args, **kwargs):
        if args in cache_storage:
            result = cache_storage[args]
            print("Getting from cache")
        else:
            cache_storage[args] = func(*args, **kwargs)
            result = cache_storage[args]
            print("Calculating new result")
        return result
    return wrapper
