from utils import COINS_OPTIONS, MENU, RESOURCES


def check_resources(ingredients, resources):
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

    return enough_water and enough_milk and enough_coffee, ",".join(not_enough)


def check_transaction(coffee_option):
    cost = coffee_option.get('cost')
    enough_coins, money = process_coins(cost)

    if not enough_coins:
        print("Sorry that's not enough money. Money refunded")
        return False, money

    print(f"Here is ${money - cost:.2f} dollars in change.")
    return True, money


def coffee_machine(resources, *args, **kwargs):
    option = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    technical_option = MACHINE_OPTIONS.get(option, None)
    if technical_option:
        return technical_option(resources)

    information_coffee = MENU.get(option, None)
    enough_resources, not_enough = check_resources(information_coffee.get('ingredients'), resources)
    if not enough_resources:
        print(f"Sorry there is not enough {not_enough}")

    successful_transaction, money = check_transaction(information_coffee)

    if successful_transaction:
        resources['money'] += money
        resources['water'] -= information_coffee.get('water', 0)
        resources['coffee'] -= information_coffee.get('coffee', 0)
        resources['milk'] -= information_coffee.get('milk', 0)
        print(f"Here is your {option} ☕️. Enjoy!")
    return coffee_machine(resources)


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
    print(f"Water: {resources['water']} ml\nMilk: {resources['milk']}ml")
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

