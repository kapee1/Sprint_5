from string import ascii_letters
from random import choice, randint


def correct_user_data_generator():
    user_data = {'name': str(choice(ascii_letters) * 6),
                 'email': str(choice(ascii_letters)) * 3 + str(
                     randint(100, 999)) + '@email.com',
                 'password': str(randint(100000, 999999))}
    return user_data

