import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example: Generate a password with default length (12 characters)
password = generate_password()
print("Generated Password:", password)
