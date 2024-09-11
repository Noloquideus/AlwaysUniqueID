import random
import string
import hashlib
import base64
import secrets
from datetime import datetime


def generate_id() -> str:
    timestamp = int((datetime.now() - datetime(2000, 1, 1, 0, 0, 0)).total_seconds() * 1000)

    random_str = ''.join(random.choices(string.ascii_letters + string.digits))

    hash_obj = hashlib.sha3_256(random_str.encode())
    hashed_str = hash_obj.digest()

    token = secrets.token_hex(16)
    combined_str = hashed_str + token.encode()
    base64_str = base64.urlsafe_b64encode(combined_str).rstrip(b'=').decode('ascii')

    count = round(len(base64_str) * 0.3)
    print(count)
    random_base64_part = ''.join(random.choices(base64_str, k=count))

    final_id = f'{timestamp}-{random_base64_part}'

    return final_id


generated_id = generate_id()
print(generated_id)
