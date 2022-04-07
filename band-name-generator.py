def band_name_generator(first_name: str, second_name: str) -> str:
    return f'Your band name could be {first_name} {second_name} !!!'


if __name__ == "__main__":
    assert band_name_generator(first_name='Test', second_name='test') == f'Your band name could be Test test !!!'
    assert band_name_generator('Test', 'test') == f'Your band name could be Test test !!!'

    print("Welcome to the Band Name Generator")

    run_again = True

    while run_again != 'n':
        city = input("What's name of the city you grew up in?\n")
        pet_name = input("What's your pet's name ?\n")
        band_name_generator(city, pet_name)
        print()
        run_again = input('Do you want run again?  Press y to run again or n exit the program. \n').lower()
