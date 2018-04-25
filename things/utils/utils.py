import string
import random
import time


def generate_token(size=6, chars=string.ascii_uppercase + string.digits):
    token = ''.join(random.choice(chars) for _ in range(size))
    token += str(int(round(time.time() * 1000)))
    return token


