from utils import COINS_OPTIONS, MENU, RESOURCES


def check_resources(option, information, resources):
    ingredients = information.get('ingredients')
    not_enough = []

    enough_water = ingredients.get('water', 0) <= resources.get('water')
    enough_milk = ingredients.get('milk', 0) <= resources.get('milk')
    enough_coffee = ingredients.get('coffee', 0) <= resources.get('coffee')

    if not enough_water:
        not_enough.append('Water')
    if not enough_milk:
        not_enough.append('Milk')
    if not enough_coffee:
        not_enough.append('Coffee')

    enough_resources = enough_water and enough_milk and enough_coffee
    if not enough_resources:
        print(f'Sorry there is not enough {",".join(not_enough)}')

    else:
        successful_transaction, money = check_transaction(information)

        if successful_transaction:
            resources['money'] += money
            resources['water'] -= information.get('ingredients').get('water', 0)
            resources['coffee'] -= information.get('ingredients').get('coffee', 0)
            resources['milk'] -= information.get('ingredients').get('milk', 0)
    return resources


def check_transaction(coffee_option):
    cost = coffee_option.get('cost')
    enough_coins, money = process_coins(cost)

    if not enough_coins:
        print("Sorry that's not enough money. Money refunded")
        return False, money
    change = money - cost
    print(f"Here is ${change:.2f} dollars in change.")
    return True, cost


def coffee_machine(resources, *args, **kwargs):
    option = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    technical_option = MACHINE_OPTIONS.get(option, None)
    if technical_option:
        return technical_option(resources)

    information_coffee = MENU.get(option, None)
    remain_resources = check_resources(option, information_coffee, resources)
    return coffee_machine(remain_resources)


def initialize():
    return dict(RESOURCES, **{'money': 0})


def process_coins(price):
    money = 0
    print('Please insert coins')
    for coin in COINS_OPTIONS:
        number_of_coins = int(input(f"How many {coin}?:\n"))
        money += number_of_coins * COINS_OPTIONS[coin]
        print(f"Current money: {money:.2f}")
    return money >= price, money


def print_report(resources, *args):
    print(f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g \nMoney: ${resources['money']:.2f}")
    return coffee_machine(resources)


def turn_off(*args):
    return print("Good bye!!!!")


MACHINE_OPTIONS = {
    'report': print_report,
    'off': turn_off,
}

if __name__ == "__main__":
    resources = initialize()
    coffee_machine(resources)

