import random
import string

length = 10

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = []

for i in range(length):
    password.append(random.choice(characters))

random.shuffle(password)

password = ''.join(password)

print("Generated password:", password)
