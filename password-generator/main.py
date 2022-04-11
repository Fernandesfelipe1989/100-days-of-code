from random import choices, shuffle


def password_generator(letters: int, symbols: int, numbers: int) -> str:
    return ""


if __name__ == "__main__":
    print("Welcome to the PyPassword Generator")
    size_letters = int(input('How many letters would you like in your password:\n'))
    size_symbols = int(input('How many symbols would you like in your password:\n'))
    size_numbers = int(input('How manu numbers would you like in your password:\n'))
    print(f"Here is your password: {password_generator(size_letters, size_symbols, size_numbers)}")