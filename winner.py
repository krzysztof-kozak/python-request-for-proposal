def decide_winner(bidders):
    max_bid = 0
    winner = ""
    for bidder in bidders:
        current_bid = bidder["bid"]

        if current_bid > max_bid:
            max_bid = current_bid
            winner = bidder["name"]

    return winner, max_bid
