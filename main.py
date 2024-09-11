import random
import string
import hashlib
import base64
from datetime import datetime


def generate_id() -> str:
    timestamp = int((datetime.now() - datetime(2000, 1, 1, 0, 0, 0)).total_seconds() * 1000)

    random_str = ''.join(random.choices(string.ascii_letters + string.digits))

    hash_obj = hashlib.sha256(random_str.encode())
    hashed_str = hash_obj.digest()

    base64_str = base64.urlsafe_b64encode(hashed_str).rstrip(b'=').decode('ascii')

    id = f'{timestamp}-{base64_str}'

    return id
