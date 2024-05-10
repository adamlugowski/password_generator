from random import choice
from string import ascii_letters, digits


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


def main():
    try:
        user_input = int(input('Enter number of characters: '))
        print("It's important that this password is shown only once")
        print(f'This is your password: {password_generator(user_input)}')
    except ValueError:
        print('You should type integer.')
    finally:
        print('Take care of your password.')


if __name__ == '__main__':
    main()
