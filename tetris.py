import pygame
import sys

# Intialize pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Tetris"
FPS = 60

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()