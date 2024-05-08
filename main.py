from random import choice
import string


def password_generator(number_of_characters):
    password_characters = []
    for _ in range(number_of_characters):
        password_characters.append(choice(string.ascii_letters))

    password = ''.join(password_characters)
    return password


print(password_generator(5))
