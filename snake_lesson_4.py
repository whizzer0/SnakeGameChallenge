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
# Snake will move in direction of last arrow key pressed, but initially we will
# set this to right arrow key (so snake starts moving left to right)
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
    win.timeout(150)


    ###
    # HANDLE USER KEY INPUT
    ###

    # Store the previous key selection for future reference
    prevKey = key

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

    # Ignore useless key selections
    # Ignore the latest key press if it is not an arrow key (or Esc key)
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_ESC]:
        key = prevKey


    ###
    # CALCULATE NEW SNAKEHEAD POSITION (Lesson 2)
    ###

    # Current key selection should now be an arrow key. This arrow key, plus
    # the snakehead's current position, can be used to calculate the new
    # co-ordinates for the snakehead as it moves one 'square'.

    # The snake is an array of 2-length arrays, e.g. = [[4,10], [4,9], [4,8]] -
    # this is also known as a 3D array.
    # snake[0][0] accesses the snakehead's y-coordinate (e.g., '4')
    # snake[0][1] accesses the snakehead's x-coordinate (e.g., '10')

    newY = snake[0][0]
    if key == KEY_DOWN:
        newY += 1
    elif key == KEY_UP:
        newY -= 1

    newX = snake[0][1]
    if key == KEY_RIGHT:
        newX += 1
    elif key == KEY_LEFT:
        newX -= 1

    # Put new snakehead co-ordinates into start of snake array (position 0)
    snake.insert(0, [newY, newX])
    # ...Snake is now longer than it should be - remember to shorten later.
    # TODO Lesson #5 (Lesson 5 start)
    # TODO Lesson #5
    # See [1].


    ###
    # IF SNAKE REACHES BORDER, MAKE IT ENTER FROM OTHER SIDE (Lesson 3)
    ###

    # For our window, the Y-axis runs from 0 to 19, the X-axis from 0 to 59. (We
    # defined this earlier at the top of this file.) However, we have also drawn
    # a border (again, see earlier), so actually the snake can move 1 to 18 in
    # the Y-axis, and from 1 to 58 in the X-axis. If the snake breaches these
    # limits, reposition snakehead so it continues from the other side:
    if snake[0][0] == 0:
        snake[0][0] = 18
    if snake[0][1] == 0:
        snake[0][1] = 58
    if snake[0][0] == 19:
        snake[0][0] = 1
    if snake[0][1] == 59:
        snake[0][1] = 1


    ###
    # IF SNAKE CROSSES ITSELF (Lesson 2)
    ###

    # [1:] refers to position 1 (i.e., the 2nd element in the array, as we
    # count from 0) and onwards.
    if snake[0] in snake[1:]:
        break


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
    # [1] Remember to decrease its length
    # remove last snake co-ordinate (its 'tail') from snake array
    last = snake.pop()

    # update display where snaketail has just been removed
    win.addch(last[0], last[1], ' ')


    ###
    # DRAW THE SNAKE (Lesson 1)
    ###

    # We can write the head with a '@' character, and ensure those parts that
    # are (no longer) the head are drawn as body ('#')
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
