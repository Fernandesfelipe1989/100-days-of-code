def multiple_analyser(number: int) -> str:
    result = str(number)
    if number % 3 == 0 and number % 5 == 0:
        result = 'FizzBuzz'
    elif number % 3 == 0:
        result = 'Fizz'
    elif number % 5 == 0:
        result = 'Buzz'
    return result


if __name__ == "__main__":
    assert multiple_analyser(1) == '1'
    assert multiple_analyser(2) == '2'
    assert multiple_analyser(3) == 'Fizz'
    assert multiple_analyser(5) == 'Buzz'
    assert multiple_analyser(15) == 'FizzBuzz'
    assert multiple_analyser(30) == 'FizzBuzz'
