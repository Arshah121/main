import random
import string

def generate_password(length=12):
    """Generate a random password with a mix of letters, digits, and symbols."""
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    # Create a pool of characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter desired password length (minimum 6): "))
        password = generate_password(password_length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
