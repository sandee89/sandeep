import random
import string

def generate_password(length=12):
    """Generate a strong and secure password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password(16)  # Generate a 16-character password
print("Generated Password:", password)