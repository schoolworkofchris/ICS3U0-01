"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (84, 183, 201)
ROAD = (69, 69, 69)

lane_x = 0
lane_x1 = 320
lane_x2 = 640
lane_x3 = 960
lane_x4 = 1280
lane_x5 = 1600
lane_x6 = 1920
lane_x7 = 2240
lane_x8 = 2560
lane_y = 580
lane_move_x = 5

spoke1 = [255, 530]
spoke2 = [275, 550]
spoke3 = [235, 550]
spoke4 = [255, 570]
spoke5 = [95, 530]
spoke6 = [115, 550]
spoke7 = [75, 550]
spoke8 = [95, 570]

wheelCycle = 0
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1820, 980)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
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
    screen.fill(BLUE)
 
    # --- Drawing code should go here
    
    # Rectangle to Seperate Sky from earth
    pygame.draw.rect(screen, WHITE, [0, 310, 1820, 680], 0)

    #Road
    pygame.draw.rect(screen, ROAD, [0, 450, 1820, 280], 0)
    pygame.draw.rect(screen, WHITE, [lane_x, lane_y, 300, 20])
    pygame.draw.rect(screen, WHITE, [lane_x1, lane_y, 300, 20])
    pygame.draw.rect(screen, WHITE, [lane_x2, lane_y, 300, 20])
    pygame.draw.rect(screen, WHITE, [lane_x3, lane_y, 300, 20])
    pygame.draw.rect(screen, WHITE, [lane_x4, lane_y, 300, 20])
    pygame.draw.rect(screen, WHITE, [lane_x5, lane_y, 300, 20])
    pygame.draw.rect(screen, WHITE, [lane_x6, lane_y, 300, 20])
    lane_x -= lane_move_x
    lane_x1 -= lane_move_x
    lane_x2 -= lane_move_x
    lane_x3 -= lane_move_x
    lane_x4 -= lane_move_x
    lane_x5 -= lane_move_x
    lane_x6 -= lane_move_x
    if lane_x <= -320:
        lane_x = 1920
    if lane_x1 <= -320:
        lane_x1 = 1920
    if lane_x2 <= -320:
        lane_x2 = 1920
    if lane_x3 <= -320:
        lane_x3 = 1920
    if lane_x4 <= -320:
        lane_x4 = 1920
    if lane_x5 <= -320:
        lane_x5 = 1920
    if lane_x6 <= -320:
        lane_x6 = 1920
    if lane_x7 <= -320:
        lane_x7 = 1920
    if lane_x8 <= -320:
        lane_x8 = 1920

    #Car
    pygame.draw.rect(screen, BLACK, [20, 500, 300, 60], 0)
    pygame.draw.rect(screen, BLACK, [60, 400, 200, 100], 0)

    pygame.draw.rect(screen, WHITE, [70, 420, 80, 60], 0)
    pygame.draw.rect(screen, WHITE, [170, 420, 80, 60], 0)
    pygame.draw.ellipse(screen, WHITE, [70, 525, 50, 50], 0)
    pygame.draw.ellipse(screen, WHITE, [230, 525, 50, 50], 0)
    
    pygame.draw.line(screen, GREEN, [255, 550], spoke1, 3)
    pygame.draw.line(screen, GREEN, [255, 550], spoke2, 3)
    pygame.draw.line(screen, GREEN, [255, 550], spoke3, 3)
    pygame.draw.line(screen, GREEN, [255, 550], spoke4, 3)

    pygame.draw.line(screen, GREEN, [95, 550], spoke5, 3)
    pygame.draw.line(screen, GREEN, [95, 550], spoke6, 3)
    pygame.draw.line(screen, GREEN, [95, 550], spoke7, 3)
    pygame.draw.line(screen, GREEN, [95, 550], spoke8, 3)

    spoke5 = [105, 530]
    spoke6 = [85, 530]
    spoke7 = [85, 565]
    spoke8 = [105, 565]

    if wheelCycle == 0:
        spoke1 = [255, 530]
        spoke2 = [275, 550]
        spoke3 = [235, 550]
        spoke4 = [255, 570]
        spoke5 = [95, 530]
        spoke6 = [115, 550]
        spoke7 = [75, 550]
        spoke8 = [95, 570]
        wheelCycle = 1
        time.sleep(0.2)

    elif wheelCycle == 1:
        spoke1 = [265, 530]
        spoke2 = [270, 565]
        spoke3 = [240, 565]
        spoke4 = [240, 530]
        spoke5 = [105, 530]
        spoke6 = [85, 530]
        spoke7 = [85, 565]
        spoke8 = [105, 565]
        wheelCycle = 0
        time.sleep(0.2)
    
    '''spoke1 = [265, 530]
    spoke2 = [270, 565]
    spoke3 = [240, 565]
    spoke4 = [240, 530]
    time.sleep(1)
    spoke1 = [255, 530]
    spoke2 = [275, 550]
    spoke3 = [235, 550]
    spoke4 = [255, 570]'''


    '''
    spoke1 = [255, 530]
    spoke2 = [275, 550]
    spoke3 = [235, 550]
    spoke4 = [255, 570]
    spoke5 = [95, 530]
    spoke6 = [115, 550]
    spoke7 = [75, 550]
    spoke8 = [95, 570]'''
   


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()