#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

class Mail:

    def __init__(self):
        self.invited_names = []
        with open("./Input/Letters/starting_letter.txt", 'r') as message:
            self.letter = message.read()
        with open("./Input/Names/invited_names.txt", 'r') as invited:
            for name in invited:
                self.invited_names.append(name.replace("\n", ""))

    def create_personalize_letter_message(self):
        for name in self.invited_names:
            message = self.letter.replace("[name]", name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'a') as letter:
                letter.write(message)

    def __repr__(self):
        return self.letter


if __name__ == "__main__":
    mail = Mail()
    mail.create_personalize_letter_message()
