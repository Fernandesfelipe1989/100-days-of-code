import string
from random import choices, shuffle

all_letter_choices = string.ascii_letters
all_symbols_choices = "@&_"
all_digits_choices = string.digits


def password_generator(letters: int, symbols: int, numbers: int) -> str:
    letters_password = choices(all_letter_choices, k=letters)
    digits_password = choices(all_digits_choices, k=numbers)
    symbols_password = choices(all_symbols_choices, k=symbols)
    password = letters_password + digits_password + symbols_password
    shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print("Welcome to the PyPassword Generator")
    size_letters = int(input('How many letters would you like in your password:\n'))
    size_symbols = int(input('How many symbols would you like in your password:\n'))
    size_numbers = int(input('How many numbers would you like in your password:\n'))
    print(f"Here is your password: {password_generator(size_letters, size_symbols, size_numbers)}")
