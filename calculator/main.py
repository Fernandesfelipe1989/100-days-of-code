LOGO = """ LOGO
"""


def divide(x, y):
    if not y:
        return "Division by zero"
    return x / y


MATH_OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": divide,
    "*": lambda x, y: x * y,
}
INVALID_MESSAGE = "Invalid operation"

if __name__ == "__main__":
    print(LOGO)
    first_number = int(input("What's the first number?\n"))
    select_operation = input("Pick an operation: \n +, -, *, or /:\n")
    second_number = int(input("What's the second number?\n"))
    math_operation = MATH_OPERATIONS.get(select_operation, None)
    output_format = "{} {} {} = ".format(first_number, select_operation, second_number)
    print(f'{output_format}{math_operation(first_number, second_number)}' if select_operation else INVALID_MESSAGE)
