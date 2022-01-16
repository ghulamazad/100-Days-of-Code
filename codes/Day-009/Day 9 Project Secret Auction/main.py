from clear_console import cls
from art import logo

print(logo)

bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bidding_finished = False
while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid? $"))

    bids[name] = price

    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if answer == 'no':
        bidding_finished = True
    elif answer == 'yes':
        cls()

find_highest_bidder(bids)
