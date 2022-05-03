import string
import random


def generate_id(length):
    alphabet = list(string.ascii_uppercase)
    device_id = ""
    for index in range(length):
        letter = random.choice(alphabet)
        device_id += letter
    return device_id
