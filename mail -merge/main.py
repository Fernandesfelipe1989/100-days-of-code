
class Mail:

    def __init__(self):
        self.invited_names = []
        with open("./Input/Letters/starting_letter.txt", 'r') as message:
            self.letter = message.read().strip()
        with open("./Input/Names/invited_names.txt", 'r') as invited:
            for name in invited:
                self.invited_names.append(name.replace("\n", ""))

    def create_personalize_letter_message(self):
        for name in self.invited_names:
            message = self.letter.replace("[name]", name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'w') as letter:
                letter.write(message)

    def __repr__(self):
        return self.letter


if __name__ == "__main__":
    mail = Mail()
    mail.create_personalize_letter_message()
