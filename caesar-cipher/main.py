from string import ascii_lowercase

LETTERS = [letter for letter in ascii_lowercase]


def encode_shit_method(letter: str, shift: int) -> str:
    if not letter in LETTERS:
        return letter

    letter_index = LETTERS.index(letter)
    letter_index += shift

    if letter_index > len(LETTERS) - 1:
        letter_index = letter_index - len(LETTERS) + 1

    return LETTERS[letter_index]


def caesar_encryption(message: str, shift: int) -> str:
    encode_message = (encode_shit_method(letter, shift) for letter in message.lower())
    return "".join(encode_message)


if __name__ == "__main__":
    user_message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))
    print(caesar_encryption(user_message, shift_number))
