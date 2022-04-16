from utils import LOGO, divide


MATH_OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": divide,
    "*": lambda x, y: x * y,
}
INVALID_MESSAGE = "Invalid operation"


def calculate(should_continue='yes'):
    if should_continue != 'yes':
        return None
    continuous_calculate = 'yes'
    first_number = float(input("What's the first number?\n"))
    answer = first_number
    while continuous_calculate == 'yes':
        select_operation = input(f"Pick an operation: {' '.join((symbol for symbol in MATH_OPERATIONS))}:\n")
        second_number = float(input("What's the next number?\n"))
        math_operation = MATH_OPERATIONS.get(select_operation, None)
        output_format = "{} {} {} = ".format(answer, select_operation, second_number)
        answer = math_operation(answer, second_number)
        print(f'{output_format}{answer}' if select_operation else INVALID_MESSAGE)
        if type(answer) == str:
            break
        continuous_calculate = input(f"Type yes to continue calculating {answer}, "
                                     f"or type n to start a new calculation:\n").lower()
    should_continue = input(f"Type yes to continue using the calculator, or type n exit:\n").lower()
    return calculate(should_continue)


if __name__ == "__main__":
    print(LOGO)
    calculate()
