# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Incorrect name!'

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Incorrect number!'    

def rpsls(player_choice):    
    print('Player chooses is: ', player_choice) 

    player = name_to_number(player_choice)

    computer = random.randrange(5)

    computer_choice = number_to_name(computer)

    print('Computer chooses is: ', computer_choice)

    difference = ((player - computer) % 5)

    if difference == 1 or difference == 2:
        print('Player wins!')
    elif difference == 3 or difference == 4:
        print('Computer wins!')
    elif difference == 0:
        print("Player and computer tie!")
    else:
        print("Incorrect input data")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



