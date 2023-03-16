from art import logo
import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

bids={}
print(logo)
#Function to find highest bid
def find_highest_bid(bidding_record):
  highest_bid=0
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner}, with a bid amount of {highest_bid}")
  
end_of_bid=True
while end_of_bid:
  name=input("Whats your name?")
  bid=int(input("Whats your bid?"))
  bids[name]=bid
  n=input("Yes there any other bidders?")
  if n == "no":
    find_highest_bid(bids)
    end_of_bid=False
  else:
    screen_clear()

