percentage_converter = {
    '10': 1.10,
    '12': 1.12,
    '15': 1.15,
}


def tip_calculator(bid: float, people: int, percentage: str) -> float:
    total = bid * percentage_converter.get(percentage, 1)
    return total/people if people else total


if __name__ == '__main__':
    print("Welcome to the tip calculator")
    total_bid = float(input('What was the total bill? $'))
    number_people = int(input("How many people to split the bill? "))
    percent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
    bid_per_person = tip_calculator(total_bid, number_people, percent_tip)
    print(f"Each person should pay: ${bid_per_person:0.1f}")
