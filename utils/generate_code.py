import random


def generate_code(length=20):
    data = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''.join(random.choice(data) for _ in range(length))
    return code

