from day_9_art import logo

print(logo)

# start an emply dictionary
bids={}

#while bidding is not finish the bidding still active.
bidding_finish =False


def find_highest_bidder(bidding_records):
    highest_bid=0
    winner = ''
    for bidder in bidding_records:
        bid_amount=bidding_records[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner = bidder
    print(f'The winner is {winner} and the bid was: {highest_bid}')



while not bidding_finish:

    name=input("What is your name?: ")
    price=int(input("What is your bid?: "))

# build the dictionay base on two inputs, name and price and expresed in dictionary way.

    bids[name]:price
#Then you create a form to exit the loop and ask the user for a reponse.
    
    should_continue=input('Are ther any other bidders?:  Type "Yes" or "No"  ')
    
    should_continue =should_continue.lower()
    
    if should_continue == 'no':
        bidding_finish = True
        find_highest_bidder(bids)
