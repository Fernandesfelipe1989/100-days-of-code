path_descriptions = {
    'first': "You're at a cross road. Where do you want to go? Type left or right ",
    'second': "You come to a lake. There is an island in the middle of the lake. Type await to wait for a boat. "
              "Type swim to swim across ",
    'third': "You arrive at the island unharmed. There is a house with 3 doors. One red, One, yellow and one blue."
             "Which colour do you choose? "
}
path_results = {
    'wrong_direction': 'Fall into a hole.\nGame Over',
    'wrong_action': 'Attacked by trout.\nGame Over',
    'third_first_wrong_door': 'Burned by fire.\nGame Over',
    'third_second_wrong_door': 'Eaten by beasts.\nGame Over',
    'third_right_door': 'You Win',
    'wrong_final': 'Game Over.',
}
conditional_options = {
    'first': 'left',
    'second': 'wait',
    'third_right_door': 'yellow',
    'third_first_wrong_door': 'red',
    'third_second_wrong_door': 'blue',
}


def treasure_path_choices():
    print("")
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
    print("Welcome to Treasure Island.\nYour mission is to find the treasure")
    print(treasure_path_choices())
