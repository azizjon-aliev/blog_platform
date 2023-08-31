import hashlib
import os
import re
import uuid


def check_phone_number(phone_number):
    return bool(re.match(r'^992\d{9}$', phone_number))


def reduce_path(file_name, times):
    result = os.path.realpath(file_name)
    for i in range(times):
        result = os.path.dirname(result)
    return result


def generate_unique_string(length):
    generated_string = str(uuid.uuid4())[:length]
    return generated_string
