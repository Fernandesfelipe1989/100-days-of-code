from string import ascii_lowercase

from utils import LOGO

LETTERS = [letter for letter in ascii_lowercase]
MAX_SIZE = len(LETTERS)


def shit_method(letter: str, shift: int, action: str) -> str:
    is_letter = letter in LETTERS

    if not is_letter:
        return letter

    if shift > MAX_SIZE or -MAX_SIZE > shift:
        shift = shift % MAX_SIZE

    letter_index = LETTERS.index(letter)
    letter_index += shift if action == 'encode' else shift * -1

    if letter_index > MAX_SIZE - 1:
        letter_index = letter_index - MAX_SIZE

    if letter_index < 0:
        letter_index -= 1

    return LETTERS[letter_index]


def caesar_cipher_process(message: str, shift: int, action: str) -> str:
    result_message = (shit_method(letter, shift, action) for letter in message.lower())
    return "".join(result_message)


if __name__ == "__main__":
    print(LOGO)
    stop_condition = "y"
    while stop_condition == "y":
        direction = input("Type encode to encrypt, or decode to decrypt:\n").lower()
        user_message = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number:\n"))

        if direction == 'encode':
            print(f"The encoded text is {caesar_cipher_process(user_message, shift_number, 'encode')}")
        elif direction == 'decode':
            print(f"The decoded text is {caesar_cipher_process(user_message, shift_number, 'decode')}")
        else:
            print('Invalid option. So bye-bye')
        stop_condition = input("Type y if you want to go again, Otherwise type n\n").lower()
