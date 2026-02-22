import random
import string

# All characters (letters + numbers + symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Password length
length = 16

# Generate password
password = "".join(random.choice(characters) for i in range(length))

print("Generated Password:", password)
