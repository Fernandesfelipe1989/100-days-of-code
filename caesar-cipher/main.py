from string import ascii_lowercase

LETTERS = [letter for letter in ascii_lowercase]


def encode_shit_method(letter: str, shift: int) -> str:
    if letter in LETTERS is False:
        return letter

    letter_index = LETTERS.index(letter)
    letter_index += shift

    if letter_index > len(LETTERS) - 1:
        letter_index = letter_index - len(LETTERS) + 1

    return LETTERS[letter_index]


def decode_shit_method(letter: str, shift: int) -> str:
    if letter in LETTERS is False:
        return letter

    letter_index = LETTERS.index(letter)
    letter_index -= shift

    if letter_index < 0:
        letter_index -= 1

    return LETTERS[letter_index]


def caesar_decryption(message: str, shift) -> str:
    decode_message = (decode_shit_method(letter, shift) for letter in message.lower())
    return "".join(decode_message)


def caesar_encryption(message: str, shift: int) -> str:
    encode_message = (encode_shit_method(letter, shift) for letter in message.lower())
    return "".join(encode_message)


if __name__ == "__main__":
    user_message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))
    encode_message = caesar_encryption(user_message, shift_number)
    print(caesar_encryption(user_message, shift_number))
    decode = caesar_decryption(encode_message, shift_number)
    print(decode)
