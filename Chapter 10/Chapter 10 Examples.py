"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK,[96-95+x,83-83+y,10,10],0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [100-95+x,100-83+y], [105-95+x,110-83+y], 2)
    pygame.draw.line(screen, BLACK, [100-95+x,100-83+y], [95-95+x,110-83+y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [100-95+x,100-83+y], [100-95+x,90-83+y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [100-95+x,90-83+y], [104-95+x,100-83+y], 2)
    pygame.draw.line(screen, RED, [100-95+x,90-83+y], [96-95+x,100-83+y], 2)
 
pygame.mouse.set_visible(0)

x_coord = 10
y_coord = 10

x_speed = 0
y_speed = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
 
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    print(pos)
    x=pos[0]
    y=pos[1]
    x_coord += x_speed
    y_coord += y_speed
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here

    draw_stick_figure(screen, 0, 0)
    draw_stick_figure(screen, x, y)
    draw_stick_figure(screen, x_coord, y_coord)

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()