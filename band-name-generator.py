
print("Welcome to the Band Name Generator")

run_again = True

while run_again != 'n':
    city = input("What's name of the city you grew up in?\n")
    pet_name = input("What's your pet's name ?\n")
    print(f'Your band name could be {city} {pet_name} !!!')
    run_again = input('Do you want run again?  Press y to run again or n exit the program. \n').lower()
