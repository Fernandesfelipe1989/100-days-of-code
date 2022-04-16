from replit import clear

from utils import LOGO

if __name__ == "__main__":
    print(LOGO)
    print("Welcome to the secret auction program")
    auction = {}
    run_auction = 'yes'
    while run_auction == 'yes':
        name = input("What's your name:\n")
        clear()
        bid = int(input("What's your bid?: $"))
        auction[bid] = name
        run_auction = input("Are there any other bidders? Type yes or no\n").lower()
    bids = (bid for bid in auction.keys())
    winner = max(bids)
    print(f"The winner is {auction[winner]} a bid of ${winner}")

