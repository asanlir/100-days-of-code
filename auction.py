# TODO-1: Ask user for input
# TODO-2: Save the data in a dictionary {name:price}
# TODO-3: Ask user if there are any other bidders
# TODO-4: Compare the bids and find the highest bidder

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| ´-´´´---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

def find_highest_bidder(bidding_dict):

    highest_bid = 0
    winner = ""

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        continue_bidding = False
        print("\n" * 100)
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)
