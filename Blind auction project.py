from art import logo
print(logo)

auction = {}
def compare(auction):
    result = 0
    final = ""
    # TODO-4: Compare bids in dictionary
    for key, value in auction.items():
        if auction[key] > result:
            result = auction[key]
            final = key
    print(f"Winner is {final} with a bid of ${result}")

while(1):
    # TODO-1: Ask the user for input
    name = input("What is your name:")
    bid = int(input("What is your bid:$"))
    # TODO-2: Save data into dictionary {name: price}
    auction[name] = bid
    print("\n" * 20)

    # TODO-3: Whether if new bids need to be added
    decision = input("Are there any bidders?Type Yes or No.").lower()
    if decision == "no":
        compare(auction)
        break
    elif decision == "yes":
        continue






