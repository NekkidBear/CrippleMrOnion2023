from cards import *
from hand import *
from CMO_settings import *
import ctypes
import pygame
import sys


# This is the main game loop for 'Cripple Mr Onion.'  Although I'm writing the implementation and architecting the code
# with assistance from Bing Chat AI, I don't own the concept/IP of the game. The game was originally suggested in the
# works of Sir Terry Pratchett. The rules were originally published in 1998 by Andrew C. Millard and Terry Tao.
#
# Currently, the rules are housed at https://discworld.fandom.com/wiki/Cripple_Mr_Onion_Full_Rules. I've also included a
# text file with them should that site go down.

def main():
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Start the clock
    clock = pygame.time.Clock()

    while True:
        # Limit the frame rate to FPS
        clock.tick(FPS)

        # Process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_data()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_data()
                    pygame.quit()
                    sys.exit()

        # Update game state
        update_game()

        # Draw everything
        draw(screen)


def save_data():
    """
    Save player data and game stats to the database.
    """
    pass


def update_game():
    """
    Update the game state.
    """
    pass


def draw(screen):
    """
    Draw everything to the screen.
    """
    pass


if __name__ == "__main__":
    main()
