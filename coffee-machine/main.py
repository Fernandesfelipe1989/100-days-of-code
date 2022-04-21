from utils import COINS_OPTIONS, MENU, RESOURCES

# TODO 1 Initial Setup and user's option:
#  - Turn off the Coffee Machine by entering “off” to the prompt:
#  - Print report:
#  - Prompt user by asking “What would you like? (espresso/latte/cappuccino):
"""
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
"""


def initialize():
    return dict(RESOURCES, **{'money': 0})


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

# TODO 2 Check resources:
"""
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""


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

# TODO 3 Process coins:
"""
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
"""


def process_coins(price):
    money = 0
    print('Please insert coins')
    for coin in COINS_OPTIONS:
        number_of_coins = int(input(f"How many {coin}?:\n"))
        money += number_of_coins * COINS_OPTIONS[coin]
    return money >= price, money
# TODO 4 Check transaction:
"""
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
"""


def check_transaction(coffee_option):
    enough_coins, money = process_coins(coffee_option.get('cost'))

    if not enough_coins:
        print("Sorry that's not enough money. Money refunded")
        return False, money

    print(f"Here is ${money:.2f} dollars in change.")
    return True, money

# TODO 5 Make Coffee
"""
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""


def coffee_machine(resources, *args, **kwargs):
    option = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    technical_option = MACHINE_OPTIONS.get(option, None)
    if technical_option:
        return technical_option(resources)

    selected_coffee_option = MENU.get(option, None)
    enough_resources, not_enough = check_resources(selected_coffee_option.get('ingredients'), resources)
    if not enough_resources:
        print(f"Sorry there is not enough {not_enough}")

    successful_transaction, money = check_transaction(selected_coffee_option)

    if successful_transaction:
        resources['money'] += money
        print(f"{resources['money']:.2f}\nMake coffee")

    return coffee_machine(resources)


if __name__ == "__main__":
    resources = initialize()
    coffee_machine(resources)

    pass
