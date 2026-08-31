# task.py
import time

def process_image(image_id):
    result = 0
    for i in range(5_000_000):
        result += (i ** 2) / 3.14159
    return result