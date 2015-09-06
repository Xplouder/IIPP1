# coding=utf-8
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

__author__ = 'João Silva'

secret_number = None
range_type = 100
max_guesses = 7
guesses_counter = 0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, max_guesses, guesses_counter
    guesses_counter = 0
    if range_type == 100:
        max_guesses = 7
        secret_number = random.randrange(0, 100)
        print "New game. Range is [0,100)"
    else:
        max_guesses = 10
        secret_number = random.randrange(0, 1000)
        print "New game. Range is [0,1000)"

    print "Number of remaining guesses is", max_guesses - guesses_counter, "\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_type
    range_type = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_type
    range_type = 1000
    new_game()


def input_guess(guess):
    global guesses_counter

    guess_int = int(guess)
    print "Guess was", guess_int
    guesses_counter += 1

    if guess_int == secret_number:
        print "Correct!\n"
        new_game()
    elif guesses_counter >= max_guesses:
        print "You ran out of guesses.  The number was", secret_number, "\n"
        new_game()
    elif guess_int > secret_number:
        print "Number of remaining guesses is", max_guesses - guesses_counter
        print "Lower!\n"
    else:
        print "Number of remaining guesses is", max_guesses - guesses_counter
        print "Higher!\n"


# create frame
frame = simplegui.create_frame("Example", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)
frame.start()

# call new_game 
new_game()
