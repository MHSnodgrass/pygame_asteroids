# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    while True:
        # If the user hits the close button (x), it will actually close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the screen to black
        screen.fill((0, 0, 0))
        # Draw the player to the screen
        player.draw(screen)
        # Refresh the display
        pygame.display.flip()
        # Pauses game loop until 1/60th of a second has passed (60 FPS)
        # Returns the amount of time that has pissed since it was last called, dividing by 1000 to get seconds and saving it to the delta
        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()