# ---------------------------------------
# Simulates a modified Liberty Bell Slot Machine
# by completing spin_payout and simulate functions.
# ---------------------------------------

import random
import sys

# Constants that represent the result of spinning a reel
DIAMOND = 1     
HEART = 2
SPADE = 3
HORSESHOE = 4
LIBERTY_BELL = 5

# ---------------------------------------
# spin_payout
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Returns an integer, the payout of the spin
# ---------------------------------------

def spin_payout(reel_1, reel_2, reel_3):

    payout = 0 # initialize payout counter

    if reel_1 == reel_2 and reel_2 == reel_3: # checks if all reels are equal
        if reel_1 == DIAMOND: # checks for triple diamonds
            payout += 30
        elif reel_1 == HEART: # checks for triple hearts
            payout += 40
        elif reel_1 == SPADE: # checks for triple spades
            payout += 20
        elif reel_1 == HORSESHOE: # checks for triple horseshoes
            payout += 10
        else:             # else must be triple liberty bells
            payout += 50

    # checks if double horseshes
    elif (reel_1 == HORSESHOE and reel_2 == HORSESHOE) or (reel_1 == HORSESHOE and reel_3 == HORSESHOE) or (reel_2 == HORSESHOE and reel_3 == HORSESHOE):
        payout += 5

    return payout
            
# ---------------------------------------
# convert
# FUNCTION PROVIDED BY PROFESSOR
# ---------------------------------------
# reel: the symbol on a reel, an integer constant
# ---------------------------------------
# Returns a string, the printing value of integer
# ---------------------------------------

def convert(reel):
    if reel == DIAMOND:
        return "diamond"
    elif reel == HEART:
        return "heart"
    elif reel == SPADE:
        return "spade"
    elif reel == HORSESHOE:
        return "horseshoe"
    elif reel == LIBERTY_BELL:
        return "bell"
    else:
        return "error!"

# ---------------------------------------
# test_known_spin
# FUNCTION PROVIDED BY PROFESSOR
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Display a message that shows the spin and its payout
# ---------------------------------------

def test_known_spin(reel_1, reel_2, reel_3):
    message = "{:10}".format(convert(reel_1))
    message += "{:10}".format(convert(reel_2))
    message += "{:10}".format(convert(reel_3))
    message += "{:-6d}".format(spin_payout(reel_1, reel_2, reel_3))
    print(message)

# ---------------------------------------
# test_known_spins
# FUNCTION PROVIDED BY PROFESSOR
# ---------------------------------------
# For testing purposes, evaluate a variety of known spins
# ---------------------------------------

def test_known_spins():
    print("{:10}{:10}{:10}{}".format("REEL 1", "REEL 2", "REEL 3", "PAYOUT"))
    print("{:10}{:10}{:10}{}".format("------", "------", "------", "------"))
    test_known_spin(LIBERTY_BELL, LIBERTY_BELL, LIBERTY_BELL)
    test_known_spin(HEART, HEART, HEART)
    test_known_spin(DIAMOND, DIAMOND, DIAMOND)
    test_known_spin(SPADE, SPADE, SPADE)
    test_known_spin(HORSESHOE, HORSESHOE, HORSESHOE)
    test_known_spin(HORSESHOE, HORSESHOE, HEART)
    test_known_spin(HORSESHOE, DIAMOND, HORSESHOE)
    test_known_spin(SPADE, HORSESHOE, HORSESHOE)
    test_known_spin(HEART, HEART, HORSESHOE)
    test_known_spin(LIBERTY_BELL, DIAMOND, SPADE)

# ---------------------------------------
# simulate
# ---------------------------------------
# how_many: the number of spins to take, an integer
# ---------------------------------------
# Simulate the Liberty Bell Slot Machine being played
# how_many times.  Calculate and print the expected winnings.
# ---------------------------------------

def simulate(how_many):
    payout_total_in_dollars = 0 # initialize payout counter
    dollars_spent = (how_many * 5) / 100 # calculate how many dollars you've spent playing
    for i in range(how_many): # loop as many times as you've played and add payout for each time to the count
        reel_1 = random.randint(1,5)
        reel_2 = random.randint(1,5)
        reel_3 = random.randint(1,5)
        payout_total_in_dollars += (spin_payout(reel_1, reel_2, reel_3)) / 100 # converts payout to dollars and updates payout counter

    payout_per_dollar = (payout_total_in_dollars / dollars_spent) # calculate payout per dollar spent
    print("For every $1 spent, you can expect to win ${:.2f}".format(payout_per_dollar))
        
# ---------------------------------------
# start_game
# ---------------------------------------
# Starts a simulatd game of Liberty Bell
# with a starting amount of money inputted
# by user, and deducts and adds money
# as user keeps playing, while letting user
# know their result each time they play.
# ---------------------------------------

def start_game(amount):

    money_left = amount
        
# lets user know current balance
    print("You currently have: ${:.2f} in your account".format(money_left))

# stops game round if user cannot afford another play
    if money_left < 0.05:
        print("You do not have enough money to keep playing.")
        
# prompts user to decide whether to play again or not, only allows Y/N answers (not case sensitive)
        while True:
            play_again = input("\nGame Ended. Do you want to play again? (Y/N)\n").upper() 
            if play_again == "N" or play_again == "Y":
                break
        if play_again =="Y":
            start_game(get_input()) # starts game again
        else:
            print("Game Ended.")
            sys.exit()

# prompts user to decide whether to play again or not, only allows Y/N answers (not case sensitive)            
    while True:
        yes_no = input("\nPlay? (Y/N)\n").upper()
        if yes_no == "N" or yes_no == "Y":
            break
        
# ends game if user chooses N
    if yes_no == "N":
        print("\nGame Ended. Your remaining balance is ${:.2f}.\n".format(money_left))
        sys.exit()

# calculates remaining balance and result of round, and starts another round of the game        
    else:
        money_left -= 0.05
        reel1 = random.randint(1,5)
        reel2 = random.randint(1,5)
        reel3 = random.randint(1,5)
        money_left += (spin_payout(reel1, reel2, reel3))/100
        print("You got a {0}, a {1}, and a {2}!".format(convert(reel1),convert(reel2), convert(reel3)))
        start_game(money_left)

# ---------------------------------------
# get_input
# ---------------------------------------
# gets valid input to begin the game
# ---------------------------------------

def get_input():

    while True:
        user_input = input("How much money do you start with? $")    
        try:
            test = float(user_input)
            break
        except ValueError:
            print("\nERROR: You must enter a number.\n")
    return test

# ---------------------------------------
# main - controls the main flow of logic
# ---------------------------------------

def main():
    print("Program 1: Liberty Bell Slot Machine Simulation\n")
    print("--> Part 1: Testing Known Spins\n")
    test_known_spins()
    print("\n--> Part 2: Simulating 500,000 Spins\n")
    simulate(500000)
    print("\n--> Part 3: Simulating an Interactive Liberty Bell Game\n")
    start_game(get_input())

# ---------------------------------------

main()
