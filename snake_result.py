################################################################################
# 'SNAKEY' GAME
## Adapted by George Deeks from https://gist.github.com/sanchitgangwar/2158089
## Use ARROW KEYS to play and Esc Key to exit
################################################################################

# Import helper libraries
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import time

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

# Key constants
KEY_ESC = 27 #Escape key reference number for the computer system
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_D = 100
VALID_KEYS = [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_ESC, KEY_W, KEY_A, KEY_S, KEY_D] #The keys that are used to control the game
OPP_KEY = {KEY_RIGHT:KEY_LEFT, KEY_LEFT:KEY_RIGHT, KEY_UP:KEY_DOWN, KEY_DOWN:KEY_UP, KEY_W:KEY_A, KEY_A:KEY_W, KEY_S:KEY_D, KEY_D:KEY_S} #A dict of opposite keys to prevent backtracking

# Constants to adjust the game difficulty
INIT_LENGTH = 6 #Change the initial length of the snake
INIT_SPEED = INIT_LENGTH #This also sets the initial speed of the snake
INIT_P2 = True #Enable second snake controlled with WASD

if not INIT_P2:
    VALID_KEYS = [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_ESC] #The keys that are used to control the game with only 1 player

################################################################################
# INITIALISING VALUES BEFORE THE GAME STARTS
################################################################################

# Initial snake co-ordinates
# Co-ordinates are y-coordinate, then x-coordinate.
# Snake is being placed here approximately in the middle left of our window
snake = []
for y in range(0, min(48,INIT_LENGTH)):
	snake.append([4, 10+min(48,INIT_LENGTH)-y])

if INIT_P2:
    snake2 = []
    for y in range(0, min(48,INIT_LENGTH)):
	    snake2.append([6, 8+min(48,INIT_LENGTH)-y])

# Initial snake direction
# Snake will move in direction of last arrow key pressed, but initially we will
# set this to right arrow key (so snake starts moving left to right)
key = KEY_RIGHT
key2 = KEY_D

# First food co-ordinates (Lesson 4)
food = [10,20]

# Display the food
# 'win' represents where we are playing our game.
# 'addch' will add a single character based on co-ordinates it receives
win.addch(food[0], food[1], '*')

# Print the game title on the top border
win.addstr(0, 27, "  SNAKEY  ")

# Initial score (Lesson 7)
score = 0


################################################################################
# THE MAIN GAME LOOP (Lesson 1)
################################################################################

# A 'while' loop will repeatedly execute until its stated condition is met, OR
# a 'break' statement is executed inside of it. Each loop iteration will execute
# one movement of the snake and update the game display accordingly. The
# condition that breaks this while loop is the user pressing the Esc key, which
# will end the game.

while key != KEY_ESC:

    # Print current 'Score' string
    win.addstr(0, 2, ' Score : ' + str(score) + ' ')


    ###
    # SET THE SPEED 'LEVEL' OF THE GAME (Lesson 8)
    ###

    # We will determine the speed of the snake based on the score:
    # 0 will be our slowest speed level
    # 120 will be our fastest speed level

    # Each time the score increases by 1, we will increase the speed level by 2
    # Therefore, speedSetting is double the score value:
    speedSetting = 2 * INIT_SPEED + 2 * score

    # We want to limit the speed level to our max, which is 120
    if speedSetting > 120:
        speedSetting = 120

    # The higher the speed level, the less time it will take for our program
    # to update the latest snake movement, and therefore the game will play
    # faster
    win.timeout(150 - speedSetting)


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
    # If SPACE BAR is pressed, then wait for another SPACE BAR to be pressed to
    # resume game.
    if key == ord(' '):

        # update display to show game is paused
        win.addstr(0, 27, " *PAUSED* ")

        # reset key to invalid value, then keep reading new key presses until
        # SPACE BAR has been pressed
        key = -1
        while key != ord(' '):
            key = win.getch()

        # Game is now resumed, so let's update display:
        win.addstr(0, 27, "  SNAKEY  ")

        # replace SPACE BAR with previous key selection, as if no SPACE BARs had
        # ever been pressed!
        key = prevKey

    # Ignore useless key selections
    # Ignore the latest key press if it is not an arrow key (or Esc key)
    if key not in VALID_KEYS or key == OPP_KEY[prevKey]:
        key = prevKey
    elif key in [KEY_W, KEY_A, KEY_S, KEY_D]:
        key2 = key
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
    # ...Snake is now longer than it should be - unless we're about to eat a
    # piece of fruit (Lesson 5). If we decide later on that we're not eating a
    # piece of fruit, we must remember to reduce the snake length by cutting off
    # its tail. See [1].
    
    #Do the same thing for the second snake if we have one.
    if INIT_P2:
        newY = snake2[0][0]
        if key2 == KEY_S:
            newY += 1
        elif key2 == KEY_W:
            newY -= 1

        newX = snake2[0][1]
        if key2 == KEY_D:
            newX += 1
        elif key2 == KEY_A:
            newX -= 1

        # Put new snakehead co-ordinates into start of snake array (position 0)
        snake2.insert(0, [newY, newX])

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
    if INIT_P2:
        if snake2[0][0] == 0:
            snake2[0][0] = 18
        if snake2[0][1] == 0:
            snake2[0][1] = 58
        if snake2[0][0] == 19:
            snake2[0][0] = 1
        if snake2[0][1] == 59:
            snake2[0][1] = 1


    ###
    # IF SNAKE CROSSES ITSELF OR ANOTHER SNAKE
    ###

    # [1:] refers to position 1 (i.e., the 2nd element in the array, as we
    # count from 0) and onwards.
    if snake[0] in snake[1:]:
        break
    
    if INIT_P2:
        if snake2[0] in snake2[1:]:
            break
        if snake[0] in snake2 or snake2[0] in snake:
            break

    ###
    # CHECK IF SNAKE HAS EATEN FOOD (Lessons 2 + 3)
    ###

    # If the snakehead co-ordinates match the current food's co-ordinates, then
    # the snake will have eaten the food!
    if snake[0] == food:
        # remove the previous food coordinates
        food = []
        # add 1 to the score
        score += 1
        # calculate new food position
        while food == []:
            food = [randint(1, 18), randint(1, 58)]
            # reset food if it's been randomly assigned a co-ordinate that the
            # snake is currently occupying
            if food in snake:
                food = []
        # update display with new food
        win.addch(food[0], food[1], '*')
    else:
        # [1] If snake does not eat food, remember to decrease its length
        # remove last snake co-ordinate (its 'tail') from snake array
        last = snake.pop()

        # update display where snaketail has just been removed
        win.addch(last[0], last[1], ' ')
    
    if INIT_P2: #Do the same thing for the other snake, if we have one
        if snake2[0] == food:
            # remove the previous food coordinates
            food = []
            # add 1 to the score
            score += 1
            # calculate new food position
            while food == []:
                food = [randint(1, 18), randint(1, 58)]
                # reset food if it's been randomly assigned a co-ordinate that the
                # snake is currently occupying
                if food in snake2:
                    food = []
            # update display with new food
            win.addch(food[0], food[1], '*')
        else:
            # [1] If snake does not eat food, remember to decrease its length
            # remove last snake co-ordinate (its 'tail') from snake array
            last = snake2.pop()

            # update display where snaketail has just been removed
            win.addch(last[0], last[1], ' ')


    ###
    # DRAW THE SNAKE (Lesson 1)
    ###

    # We can write the head with a '@' character, and ensure those parts that
    # are (no longer) the head are drawn as body ('#')
    win.addch(snake[1][0], snake[1][1], '#')
    win.addch(snake[0][0], snake[0][1], '@')
    
    if INIT_P2:
        win.addch(snake2[1][0], snake2[1][1], '£')
        win.addch(snake2[0][0], snake2[0][1], '@')


#### End of main game loop ###


################################################################################
# END OF GAME
################################################################################

# Show how the player lost for 3 seconds
start_time = time.time()
for tim in range(1,6):
    while start_time + tim > time.time():
        if tim % 2 == 0:
            win.addstr(0, 27, " INS COIN ")
        else:
            win.addstr(0, 27, " YOU LOSE ", curses.A_STANDOUT)
        win.refresh()

# Close window
curses.endwin()

# Print out score and thank you message
# Each print command will print its message to a new line
print("Final score: " + str(score))
print("Thank you for playing!")


################################################################################
### THANKS FOR PLAYING #########################################################
################################################################################
