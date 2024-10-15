import functools

__all__ = ["my_sum", "factorial"]

# add comment


@functools.cache
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot
