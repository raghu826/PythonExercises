import random
import string


def password_generator(length):

    password = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    result = ''.join(random.choice(password) for i in range(length))

    print(result)

password_generator(8)
