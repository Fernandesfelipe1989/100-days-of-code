from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    coffee_machine = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    while True:
        option = input(f"What would you like? {menu.get_items()}:\n").lower()
        available_drink = menu.find_drink(option)
        if option == "report":
            coffee_machine.report()
        elif option == 'off':
            break
        elif available_drink:
            (
                coffee_machine.is_resource_sufficient(drink=available_drink) and
                money_machine.make_payment(available_drink.cost) and
                coffee_machine.make_coffee(order=available_drink)
            )
