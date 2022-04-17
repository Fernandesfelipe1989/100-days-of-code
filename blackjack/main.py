"""
############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""


from random import choice, choices

from utils import DECK, LOGO


def calculate_score(cards):
    return sum(cards)


def dealer_card_process(card):
    score = calculate_score(card)
    if score >= 18:
        return card
    card.append(hit_card())
    return dealer_card_process(card)


def initialize():
    return choices(DECK, k=2), choices(DECK, k=2)


def hit_card():
    return choice(DECK)


if __name__ == "__main__":
    print(LOGO)
    final_message = "Draw"
    user_card, dealer_card = initialize()
    user_score = calculate_score(user_card)
    hit = 'yes'
    print(f'Your cards: {user_card}')
    print(f'Your score is: {user_score}')
    print(f"Computer's first card: {dealer_card[0]}")
    if user_card == 21:
        print('You win')
    else:
        while hit == "yes" and user_score <= 21:
            hit = input("Type yes to get another card, type no to pass:\n").lower()
            if hit == 'yes':
                user_card.append(hit_card())
                print(f'Your cards: {user_card}')
                user_score = calculate_score(user_card)
                print(f'Your score is: {user_score}')
        dealer_card = dealer_card_process(dealer_card)
        dealer_score = calculate_score(dealer_card)
        if dealer_score < user_score <= 21 or dealer_score > 21:
            final_message = "You win"
        elif user_score < dealer_score or user_score > 21:
            final_message = "Dealer win"
        print(f'Your cards: {user_card}')
        print(f'Your score is: {user_score}')
        print(f"Dealer's card: {dealer_card}")
        print(f"Dealer's score is: {dealer_score}")
        print(final_message)
