from random import random

def generate_teddys_age():
    random_number = 0
    while random_number < 20 or random_number > 100:
        random_number = random() * 100

    print(f"Teddy is {int(random_number)} years old!")
    
generate_teddys_age()
