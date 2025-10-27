bidder_name= input("What is your name?\n")
bid= int(input("What is your bid: $"))
bids= {
    bidder_name: bid,
}

other_bids = True

while other_bids:
    add_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if add_bid == 'yes':
        bidder_name = input("What is your name?\n")
        bid = int(input("What is your bid: $"))
        bids[bidder_name]=bid
        print(bids)
    else:
        max_bid = max(bids, key=bids.get)
        if max_bid in bids:
            print(f"The winner is {max_bid}, with a bid of {bids[max_bid]}")
        other_bids = False