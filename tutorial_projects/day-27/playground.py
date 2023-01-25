def add(*args):
    total = 0
    for n in args:
        total += n
    return total


def calculate(n, **kwargs):
    result = n
    result += kwargs["add"]
    result *= kwargs["multiply"]
    return result
