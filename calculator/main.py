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
    run_process = "yes"
    while run_process == 'yes':
        continuous_calculate = 'yes'
        first_number = int(input("What's the first number?\n"))
        answer = first_number
        while continuous_calculate == 'yes':
            select_operation = input(f"Pick an operation: {' '.join((symbol for symbol in MATH_OPERATIONS))}:\n")
            second_number = int(input("What's the second number?\n"))
            math_operation = MATH_OPERATIONS.get(select_operation, None)
            output_format = "{} {} {} = ".format(answer, select_operation, second_number)
            answer = math_operation(answer, second_number)
            print(f'{output_format}{answer}' if select_operation else INVALID_MESSAGE)
            continuous_calculate = input(f"Type yes to continue calculating {answer}, "
                                         f"or type n to start a new calculation:\n")
        run_process = input(f"Type yes to continue using the calculator, or type n exit:\n")
