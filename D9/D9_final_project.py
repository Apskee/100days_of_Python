#Goal of this project is to create a silent auction, users will input their names and amout which they want to bid a each user will have an empty screen
#so they dont see each other, at the end of the auction winner will be determined judgind by the highest amount they bid.


##### SOLUTION #####

#Importing library
from os import system
 
bidding = True #Variable determining is while loop continues or not
bids = {} #Empty dictionary

#Fuction that find the highest value
def max_bid_value(bids):
    highest_bid = int() #Empty variable to store highest value
    for bidder in bids: #For loop to loop through each bidder
        bid_amount = bids[bidder] #Assigning bidder to a variable
        if bid_amount > highest_bid: #Comparing bidder's value with previous value
            highest_bid = bid_amount #Assigning new highest value
            winner = bidder
    print(f"The winner is {winner} with an amount of {highest_bid}")

#While loop getting inputs
while bidding == True:
    name = input("What is your name? ")
    amount = input("What is the amount you would like to bid ? $")
    bids[name] = int(amount)
    other_users = input("Is there any other bidder? 'Yes' or 'No'? ") #Checking if there are other players 
    if other_users == "No":  #If no cancel the while loop
        bidding = False
        max_bid_value(bids)
    else:
        system("clear")




