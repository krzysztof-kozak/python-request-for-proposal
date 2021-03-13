from replit import clear
from art import logo
from winner import decide_winner

bidders = []
next_round = True
while next_round:
    clear()
    print(logo)
    print("Hello Vendor. Welcome to the RFP program\n")

    name = input("What is your legal entity name? ")
    bid = int(input("What is your bid? $"))
    other_bidders = input("\nAdministrator, are there any other bidders(y or n)? ")

    bidders.append({
        "name": name,
        "bid": bid,
    })

    if other_bidders.lower() != "y":
        next_round = False
        print(bidders)
        winner, bid = decide_winner(bidders)

        clear()
        print(logo)

        print(f"The winner is {winner} with a bid of ${bid}")
