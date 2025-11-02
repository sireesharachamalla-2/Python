import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_until_match(target):
    attempts = 0
    while True:
        attempts += 1
        guess = generate_random_string(len(target))
        print(f"Attempt {attempts}: {guess}")
        if guess == target:
            print(f"Matched target '{target}' in {attempts} attempts!")
            break
target = "abc"
generate_until_match(target)