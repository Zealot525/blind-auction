from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program!")
auction = {}
to_finish = False

while not to_finish:
    bidder = input("Type the name of the bidder:\n")
    amount = input("Type the amount of the bid:\n$")
    auction[bidder] = amount
    anyone_else = input("Is there anyone else who wants to bid? Type 'yes' or 'no':\n").lower()
    if anyone_else =="no":
        to_finish = True
        print(f"The winner is {max(auction, key=auction.get)} with a bid of ${max(auction.values())}")
    else:
        clear()
