import pygame
import sys

# Grid settings
GRID_WIDTH = 10 # Number of columns
GRID_HEIGHT = 20 # Number of rows
CELL_SIZE = 30 # Size of each cell in pixels

# Intialize pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
WINDOW_TITLE = "Tetris"
FPS = 60

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to draw grid lines
# Iterate over each column (x) and row (y) and draw a rectangle for each cell
# The rectangle is drawn with a 1 pixel border
def draw_grid():
    for x in range(0, GRID_WIDTH * CELL_SIZE, CELL_SIZE):
        for y in range(0, GRID_HEIGHT * CELL_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (40, 40, 40), rect, 1) # Gray grid lines

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the grid
        draw_grid()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()