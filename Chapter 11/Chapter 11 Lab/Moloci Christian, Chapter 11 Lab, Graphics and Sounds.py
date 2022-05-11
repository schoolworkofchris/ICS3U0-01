'''
Programmed By Christian Moloci
Chapter 11 Lab

This lab demostrates the use of drawing and real image graphics.
This lab demonstrates the use of sounds.

view assignment here: http://programarcadegames.com/index.php?chapter=lab_bitmapped_graphics&lang=en
'''

from pygame import mixer
import pygame
pygame.init() 
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PLATFORM = (115, 59, 0)
COIN_WHITE = (246, 246, 246)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chris's Mario Rip Off")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Image Loading
bg = pygame.image.load("bg.png").convert()
player = pygame.image.load("mario.png").convert()
coin = pygame.image.load("coin.png").convert()
coin_sound = pygame.mixer.Sound("coin.wav")
song = pygame.mixer.Sound("song.wav")

player.set_colorkey(WHITE)
coin.set_colorkey(COIN_WHITE)

def platform(screen, platform_x, platform_y):
    pygame.draw.rect(screen, PLATFORM, [platform_x, platform_y, 200, 50], 0)
 
pygame.mouse.set_visible(False)
song.play()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            coin_sound.play()
 
    # --- Game logic should go here
    # Player Mechanics
    player_pos = pygame.mouse.get_pos()
    player_x = player_pos[0]
    player_y = player_pos[1]
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(bg, [0, 0])
 
    # --- Drawing code should go here
    platform(screen, 150, 400)
    platform(screen, 400, 250)
    platform(screen, 800, 450)

    screen.blit(coin, [180, 330])
    screen.blit(coin, [230, 330])
    screen.blit(coin, [280, 330])
    
    screen.blit(coin, [840, 380])
    screen.blit(coin, [890, 380])
    screen.blit(coin, [940, 380])

    screen.blit(player, [player_x, player_y])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()