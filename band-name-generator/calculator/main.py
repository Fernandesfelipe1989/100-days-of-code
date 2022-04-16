LOGO = """ LOGO
"""

MATH_OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
}


if __name__ == "__main__":
    print(LOGO)
    first_number = int(input("What's the first number?\n"))
    second_number = int(input("What's the second number?\n"))
    select_operation = input("Type + to sum , - to sub, * to mul, or / to divide the numbers:\n")
    math_operation = MATH_OPERATIONS.get(select_operation, None)
    print(math_operation(first_number, second_number) if select_operation else "Invalid operation")
