''' 
Programmed By Christian Moloci
Chapter 6 Lab
This Lab is about functions hence why it has so many of them
this lab is done with instructions and resources from the following webpage: http://programarcadegames.com/index.php?chapter=lab_loopy_lab&lang=en
'''

# import libraries
import pygame

# 6.1
# Ouputs a triangle with increasing numbers

# startValue is the starting value
startValue = 10
# Loops until 10 different sized rows have been created
for row in range(10):
    # Loop in charge of length of row and incrementing the startValue Var
    for digit in range(row):
        # Prints each digit
        print(startValue, end=" ")
        # adds 1 to startValue
        startValue += 1
    # Prints a space between each row so that we dont end up with one large line
    print()

print()
#6.2

# assigns the user input to the o_amount of o's desired in the box
o_amount = int(input("Enter the size of the O box you want."))

# prints the header (or top row) of o's
for amount_of_O in range(o_amount):
    print("oo", end="")

#creates a new line so that o's dont show up on same line
print()

#prints the left and right o's with the correct amount of spaces in between then starts a new line and does the same until it is finished
for amount_of_O in range(o_amount - 2):
    print("o", end="  ")
    for amount_of_o in range(o_amount -2):
        print(end="  ")
    print("o")

#prints the footer of thebottow row of o's
for amount_of_O in range(o_amount):
    print("oo", end="")

print("\n")

#6.3
# Part three

# I eventuall decided to leave this as is as this was taking too long and I have to move on (I tried three different approaches)
# Here is what I did manage to do however
# I could probably come back to this at a later point when I have spare time though.

# asks user for input on size
row_size = int(input("Please Enter the size of the box: "))

# runs some math to set things up
actual_row_size = row_size * 2

# define some vars for program
left1 = 1
left2 = 1
start_valueL = 1
start_valueR = 1

# Main loop to print the rows
for rows in range(1 , actual_row_size, 1):
    # Prints columns with the wanted nums for top half
    for column in range(start_valueL, actual_row_size, 2):
        print(left1, end=" ")
        left1 += 2
    # some changes need to be made to some vars
    left2 = left1
    left2 -= 2
    left1 = 1
    #prints columns with the wanted nums for bottom half
    for column in range(actual_row_size, left2, 1):
        print(left2, end=" ")
        left2 -= 2
    start_valueL += 2
    left1 = start_valueL
    #prints a line break before repeating and moving on to the next row
    print()


# 6.4

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#vars
square_x = 0
square_y = 0
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("6.4 Example")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for square_x in range(1, 800, 25):
        for square_y in range(1, 700, 25):
            pygame.draw.rect(screen, GREEN, [square_x, square_y, 20, 20], 0)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
