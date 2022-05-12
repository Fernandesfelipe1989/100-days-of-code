path_descriptions = {
    'first': "You're at a cross road. Where do you want to go? Type left or right\n",
    'second': "You come to a lake. There is an island in the middle of the lake. Type await to wait for a boat. "
              "Type swim to swim across\n",
    'third': "You arrive at the island unharmed. There is a house with 3 doors. One red, One, yellow and one blue."
             "Which colour do you choose?\n"
}
path_results = {
    'wrong_direction': 'Fall into a hole.\nGame Over',
    'wrong_action': 'You get attacked by an angry trout.\nGame Over.',
    'third_first_wrong_door': 'Burned by fire.\nGame Over',
    'third_second_wrong_door': 'Eaten by beasts.\nGame Over',
    'third_right_door': 'You found the treasure! You Win!',
    'wrong_final': "You chose a door that doesn't exist. Game Over.",
}
conditional_options = {
    'first': 'left',
    'second': 'wait',
    'third_right_door': 'yellow',
    'third_first_wrong_door': 'red',
    'third_second_wrong_door': 'blue',
}


def treasure_path_choices():
    turn = input(path_descriptions['first']).lower()
    if turn != conditional_options['first']:
        return path_results['wrong_direction']
    action = input(path_descriptions['second']).lower()
    if action != conditional_options['second']:
        return path_results['wrong_action']
    door = input(path_descriptions['third']).lower()
    if door == conditional_options['third_right_door']:
        return path_results['third_right_door']
    elif door == conditional_options['third_first_wrong_door']:
        return path_results['third_first_wrong_door']
    elif door == conditional_options['third_second_wrong_door']:
        return path_results['third_second_wrong_door']
    return path_results['wrong_final']


if __name__ == '__main__':
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.\nYour mission is to find the treasure")
    print(treasure_path_choices())
