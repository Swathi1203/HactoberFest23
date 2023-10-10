import random
import string

def generate_password(length=12):
    # Define characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Usage
if __name__ == "__main__":
    password_length = 12  # You can change the desired password length
    random_password = generate_password(password_length)
    print("Random Password:", random_password)
