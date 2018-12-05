# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


try: import simplegui except ImportError: import SimpleGUICS2Pygame.simpleguics2pygame as simplegui 
import random
import math




###################################################
# Start our test #1 - assume global variable secret_number
# is the the "secret number" - change name if necessary

rrange = 100

def input_guess(guess):
    
    global tries

    if tries == 1:
        label1.set_text('game is over! Secret Number is: %d' % secret_number)
        print('game is over! Secret Number is: %d' % secret_number)
        new_game(rrange)
        
    else:
        tries = tries - 1
        
        label_try.set_text('%d tries to end' % tries)

        print('Guess was %d' % guess )

        guess = int(guess)

        if guess == secret_number:
            label1.set_text('%d is Correct.\nYou may play another game. The random number has generated' % guess)
            new_game(rrange)

        elif guess < secret_number:
            label1.set_text('%d is Lower'% guess)

        else:
            label1.set_text('%d is Higher' %guess)
    

def clear_input():
    
    input_guess(inp.get_text())
    inp.set_text('')
    label3.set_text('')
    

def new_game(rrange):
    
    label2.set_text('Current range is [0:%d)' % rrange)
    
    print('New game')
    global secret_number 
    secret_number = random.randrange(0, rrange)
    label3.set_text('')
    
    global tries
    tries = math.ceil(math.log(rrange,2))
    label_try.set_text('%d to end' %tries )

def change_range_100():
    
    label2.set_text('Current range is [0:100)')
    new_game(100)


def change_range_1000():
    
    label2.set_text('Current range is [0:1000)')
    new_game(1000)


frame = simplegui.create_frame('Guessing', 200, 300, 500)

label2 = frame.add_label('Current range is [0:100)', 500)
label_try = frame.add_label('', 500)

inp = frame.add_input('Input guess', input_guess, 250)

button1 = frame.add_button('Next try...', clear_input)

label1 = frame.add_label('', 500)

label3 = frame.add_label('', 500)

# "Rangeis[0,100)"
button3 = frame.add_button('Try Rangeis[0,100)', change_range_100)

# "Rangeis[0,1000)"
button4 = frame.add_button('Try Rangeis[0,1000)', change_range_1000)


###################################################
# Output from test #1
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Higher!
#
#Guess was 75
#Number of remaining guesses is 5
#Lower!
#
#Guess was 62
#Number of remaining guesses is 4
#Higher!
#
#Guess was 68
#Number of remaining guesses is 3
#Higher!
#
#Guess was 71
#Number of remaining guesses is 2
#Higher!
#
#Guess was 73
#Number of remaining guesses is 1
#Higher!
#
#Guess was 74
#Number of remaining guesses is 0
#Correct!
#
#New game. Range is [0,100)
#Number of remaining guesses is 7

###################################################
# Start our test #2 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range1000()
#secret_number = 375    
#input_guess("500")
#input_guess("250")
#input_guess("375")

###################################################
# Output from test #2
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#New game. Range is [0,1000)
#Number of remaining guesses is 10
#
#Guess was 500
#Number of remaining guesses is 9
#Lower!
#
#Guess was 250
#Number of remaining guesses is 8
#Higher!
#
#Guess was 375
#Number of remaining guesses is 7
#Correct!
#
#New game. Range is [0,1000)
#Number of remaining guesses is 10



###################################################
# Start our test #3 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range100()
#secret_number = 28 
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")

###################################################
# Output from test #3
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Lower!
#
#Guess was 50
#Number of remaining guesses is 5
#Lower!
#
#Guess was 50
#Number of remaining guesses is 4
#Lower!
#
#Guess was 50
#Number of remaining guesses is 3
#Lower!
#
#Guess was 50
#Number of remaining guesses is 2
#Lower!
#
#Guess was 50
#Number of remaining guesses is 1
#Lower!
#
#Guess was 50
#Number of remaining guesses is 0
#You ran out of guesses.  The number was 28
#
#New game. Range is [0,100)
#Number of remaining guesses is 7

