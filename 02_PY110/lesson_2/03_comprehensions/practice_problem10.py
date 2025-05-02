import string
import random

def generate_uuid():
    def generate_subcomponent(amount_of_chars):
       return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(amount_of_chars))

    uuid = []
    for amount in [8, 4, 4, 4, 12]:
        chars = generate_subcomponent(amount)
        uuid.append(chars)

    return '-'.join(uuid)

print(generate_uuid())