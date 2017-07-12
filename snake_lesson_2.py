################################################################################
# 'SNAKEY' GAME
## Adapted by George Deeks from https://gist.github.com/sanchitgangwar/2158089
## Use ARROW KEYS to play and Esc Key to exit
################################################################################

# Import helper libraries
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Initialise cursor and window properties
curses.initscr()
# game window will be 20 units top to bottom, and 60 units left to right
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
# draw a border for our window
win.border(0)
win.nodelay(1)

# Escape key reference number for the computer system
KEY_ESC = 27


################################################################################
# INITIALISING VALUES BEFORE THE GAME STARTS
################################################################################

# Initial snake co-ordinates
# Co-ordinates are y-coordinate, then x-coordinate.
# Snake is being placed here approximately in the middle left of our window
snake = [[4,10], [4,9], [4,8]]

# Initial snake direction
# TODO Lesson #2
# TODO Lesson #2
key = KEY_RIGHT

# TODO Lesson #4 (Start of Lesson 4)
# TODO Lesson #4

# TODO Lesson #4
# TODO Lesson #4
# TODO Lesson #4
# TODO Lesson #4

# Print the game title on the top border
win.addstr(0, 27, "  SNAKEY  ")

# Initial score (Lesson 7)
# TODO Lesson #7


################################################################################
# THE MAIN GAME LOOP (Lesson 1)
################################################################################

# A 'while' loop will repeatedly execute until its stated condition is met, OR
# a 'break' statement is executed inside of it. Each loop iteration will execute
# one movement of the snake and update the game display accordingly. The
# condition that breaks this while loop is the user pressing the Esc key. which
# will end the game.

while key != KEY_ESC:

    # TODO Lesson #7
    # TODO Lesson #7


    ###
    # SET THE SPEED 'LEVEL' OF THE GAME (Lesson 8)
    ###

    # TODO Lesson #8
    # TODO Lesson #8
    # TODO Lesson #8

    # TODO Lesson #8
    # TODO Lesson #8
    # TODO Lesson #8

    # TODO Lesson #8
    # TODO Lesson #8
    # TODO Lesson #8

    # TODO Lesson #8
    # TODO Lesson #8
    # TODO Lesson #8
    # TODO Lesson #2


    ###
    # HANDLE USER KEY INPUT
    ###

    # TODO Lesson #2
    # TODO Lesson #2

    # Determine if a valid new key has been pressed.
    event = win.getch()
    # If the new key press is invalid, the program will return -1, otherwise
    # we will update our active key pressed selection:
    if event != -1:
        key = event

    # Pause/Resume game (Lesson 6)
    # TODO Lesson #6
    # TODO Lesson #6
    # TODO Lesson #6

        # TODO Lesson #6
        # TODO Lesson #6

        # TODO Lesson #6
        # TODO Lesson #6
        # TODO Lesson #6
        # TODO Lesson #6
            # TODO Lesson #6

        # TODO Lesson #6
        # TODO Lesson #6

        # TODO Lesson #6
        # TODO Lesson #6
        # TODO Lesson #6

    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2


    ###
    # CALCULATE NEW SNAKEHEAD POSITION (Lesson 2)
    ###

    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2

    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2

    # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2

    # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2

    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #5 (Lesson 5 start)
    # TODO Lesson #5
    # TODO Lesson #2


    ###
    # IF SNAKE REACHES BORDER, STOP PROGRAM (Change to continue in Lesson 3)
    ###

    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2


    ###
    # IF SNAKE CROSSES ITSELF (Lesson 2)
    ###

    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2
        # TODO Lesson #2


    ###
    # CHECK IF SNAKE HAS EATEN FOOD (Lessons 2 + 3)
    ###

    # TODO Lesson #4
    # TODO Lesson #4
    # TODO Lesson #4
        # TODO Lesson #4
        # TODO Lesson #4
        # TODO Lesson #7
        # TODO Lesson #7
        # TODO Lesson #4
        # TODO Lesson #4
            # TODO Lesson #4
            # TODO Lesson #4
            # TODO Lesson #4
            # TODO Lesson #4
                # TODO Lesson #4
        # TODO Lesson #4
        # TODO Lesson #4
    # TODO Lesson #5
    # TODO Lesson #2
    # TODO Lesson #2
    # TODO Lesson #2

    # TODO Lesson #2
    # TODO Lesson #2


    ###
    # DRAW THE SNAKE (Lesson 1)
    ###

    # We can write the head with a '@' character, and
    # the first 'unit' of body with a '#' character
    win.addch(snake[1][0], snake[1][1], '#')
    win.addch(snake[0][0], snake[0][1], '@')


#### End of main game loop ###


################################################################################
# END OF GAME
################################################################################

# Close window
curses.endwin()

# Print out thank you message
# TODO Lesson #7
# TODO Lesson #7
print("Thank you for playing!")


################################################################################
### THANKS FOR PLAYING #########################################################
################################################################################
