# My module
cache = []

def add(num1: int, num2: int):
    res = num1 + num2

    cache.append(res)

    return res