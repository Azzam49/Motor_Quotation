import random
import string

def generate_password():
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(8))
    return password