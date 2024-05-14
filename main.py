from getpass import getpass
from random import choice
from string import ascii_letters, digits
import datetime


def password_generator(number_of_characters):
    """
    This function is creating the password using randomly chosen big letters, small letters and digits
    :param number_of_characters: Number of characters that password should have
    :return: Random password
    """
    list_of_characters = []
    password_characters = ascii_letters + digits
    for _ in range(number_of_characters):
        list_of_characters.append(choice(password_characters))

    password = ''.join(list_of_characters)

    return password


def save(password):
    """
    This function provides saving password in text file named dynamically based on timestamp
    :param password: This is password generated in password_generator
    :return: Saving in file
    """
    timestamp = timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'password_{timestamp}.'
    with open(filename, mode='w') as file:
        file.write(password)


def main():
    try:
        user_input = int(getpass('Enter number of characters: '))
        if user_input <= 0:
            raise ValueError("Number of characters should be a positive integer.")
        password = password_generator(user_input)
        if user_input > 100:
            user_input = 100
            print('Maximum password length is 100 characters. Generating password with 100 characters.')
        save(password)
    except ValueError as e:
        print(str(e))
    finally:
        print('Password was saved in password.txt file')


if __name__ == '__main__':
    main()
