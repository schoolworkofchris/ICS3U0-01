'''
Chapter 10 Lab
Programmed By Christian Moloci

Made using pygame base template
http://programarcadegames.com/python_examples/f.php?file=pygame_base_template.py

Purpose: Create a program that can control two objects. One with the mouse, one with the keyboard.

See assignment here: http://programarcadegames.com/index.php?chapter=lab_user_control&lang=en
'''
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY = (135, 206, 235)
CHOPPER = (203, 83, 54)
CAR = (197, 218, 29)
ROAD = (66, 67, 61)

# Keyboard base vars
x_keyboard_coord = 50
y_keyboard_coord = 350

# Kyboard stepping momentum
x_keyboard_speed = 0
y_keyboard_speed = 0

#Function for the helicopter
def chopper(screen, x_pos, y_pos):
    # Tail Fin
    pygame.draw.line(screen, BLACK, [x_pos- 40, y_pos-2], [x_pos-40, y_pos+25], 2)
    # Tail
    pygame.draw.line(screen, BLACK, [x_pos- 40, y_pos+12], [x_pos, y_pos+12], 2)
    # Prop Beam
    pygame.draw.line(screen, BLACK, [x_pos + 18, y_pos + 10], [x_pos + 18, y_pos-15], 2)
    # Prop
    pygame.draw.line(screen, BLACK, [x_pos+2, y_pos-15], [x_pos+35, y_pos-15], 2)
    #Body
    pygame.draw.ellipse(screen, CHOPPER, [x_pos, y_pos, 40, 25], 0)

#Function for airplane
def car(screen, x_keyboard_coord, y_keyboard_coord):
    pygame.draw.rect(screen, CAR, [x_keyboard_coord, y_keyboard_coord, 100, 60], 0)
    pygame.draw.polygon(screen, CAR, [[x_keyboard_coord, y_keyboard_coord+35], [x_keyboard_coord-30, y_keyboard_coord + 35], [x_keyboard_coord, y_keyboard_coord]], 0)
    pygame.draw.rect(screen, CAR, [x_keyboard_coord-30, y_keyboard_coord+35, 35, 25], 0)
    pygame.draw.polygon(screen, CAR, [[x_keyboard_coord+100, y_keyboard_coord+35], [x_keyboard_coord+160, y_keyboard_coord + 35], [x_keyboard_coord+100, y_keyboard_coord]], 0)
    pygame.draw.rect(screen, CAR, [x_keyboard_coord+100, y_keyboard_coord+35, 60, 25], 0)
    pygame.draw.circle(screen, BLACK, (x_keyboard_coord+10, y_keyboard_coord+60), 20)
    pygame.draw.circle(screen, BLACK, (x_keyboard_coord+110, y_keyboard_coord+60), 20)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Car vs Helicopter")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Makes Mouse invisible
pygame.mouse.set_visible(0)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Handles keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_keyboard_speed = -3
            if event.key == pygame.K_RIGHT:
                x_keyboard_speed = 3
            if event.key == pygame.K_UP:
                y_keyboard_speed = -3
            if event.key == pygame.K_DOWN:
                y_keyboard_speed = 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_keyboard_speed = 0
            if event.key == pygame.K_RIGHT:
                x_keyboard_speed = 0
            if event.key == pygame.K_UP:
                y_keyboard_speed = 0
            if event.key == pygame.K_DOWN:
                y_keyboard_speed = 0
 
    # --- Game logic should go here
    
    #Handles the mouse stuff
    pos = pygame.mouse.get_pos()

    x_pos = pos[0]
    y_pos = pos[1]

    # Handles the Keyboard stuff
    x_keyboard_coord += x_keyboard_speed
    y_keyboard_coord += y_keyboard_speed

    # conditions to handle putting the car back on the screen when it goes off screen
    if x_keyboard_coord < -180:
        x_keyboard_coord = 780
    elif x_keyboard_coord > 800:
        x_keyboard_coord = -140
    if y_keyboard_coord < -50:
        y_keyboard_coord = 480
    elif y_keyboard_coord > 550:
        y_keyboard_coord = 1

    # Sets up font for use later in program
    font = pygame.font.SysFont('comicsansms', 60, True, False)

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SKY)
 
    # --- Drawing code should go here
    
    # Road
    pygame.draw.rect(screen, ROAD, [0, 400, 700, 100], 0)

    # Draws the chopper
    chopper(screen, x_pos, y_pos)

    # Draws the car
    car(screen, x_keyboard_coord, y_keyboard_coord)
    
    # Renders the text
    text = font.render("Car vs Helicopter", True, BLACK)
    screen.blit(text, [90, 200])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()