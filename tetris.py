import pygame
import sys

# Grid settings
GRID_WIDTH = 10 # Number of columns
GRID_HEIGHT = 20 # Number of rows
CELL_SIZE = 30 # Size of each cell in pixels

# Fall interval in milliseconds
FALL_SPEED = 500 # Tetromino falls every 500 milliseconds

# Grid to track locked blocks
def create_locked_grid():
    return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

locked_grid = create_locked_grid()

# Tetromino shapes
SHAPES = {
    "I": [
        [(0, 0), (1, 0), (2, 0), (3, 0)], # Horizontal
        [(0, 0), (0, 1), (0, 2), (0, 3)]  # Vertical
    ],
    "O": [
        [(0, 0), (1, 0), (0, 1), (1, 1)] # Square
    ],
    "T": [
        [(1, 0), (0, 1), (1, 1), (2, 1)], # T-shape
        [(1, 0), (0, 1), (1, 1), (1, 2)], # T-shape rotated
        [(0, 1), (1, 1), (2, 1), (1, 2)], # T-shape rotated
        [(1, 0), (1, 1), (0, 2), (1, 2)]  # T-shape rotated
    ],
    "S": [
        [(1, 0), (2, 0), (0, 1), (1, 1)], # S-shape
        [(0, 0), (0, 1), (1, 1), (1, 2)]  # S-shape rotated
    ],
    "Z": [
        [(0, 0), (1, 0), (1, 1), (2, 1)], # Z-shape
        [(1, 0), (0, 1), (1, 1), (0, 2)]  # Z-shape rotated
    ],
    "J": [
        [(0, 0), (0, 1), (1, 1), (2, 1)], # J-shape
        [(1, 0), (2, 0), (1, 1), (1, 2)], # J-shape rotated
        [(0, 1), (1, 1), (2, 1), (2, 2)], # J-shape rotated
        [(1, 0), (1, 1), (0, 2), (1, 2)]  # J-shape rotated
    ],
}

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
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if locked_grid[y][x]:
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, locked_grid[y][x], rect)  # Fill with the block color
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Add a border
            else:
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (40, 40, 40), rect, 1)  # Draw empty grid lines

# Function to draw a tetromino
# The tetromino is drawn by iterating over each cell in the shape and drawing a rectangle
def draw_tetromino(shape, position, color):
    for row_index, row in enumerate(shape):
        for col_index, cell in enumerate(row):
            if cell: # Only draw the cell if the value is not 0
                x = (position[0] + col_index) * CELL_SIZE
                y = (position[1] + row_index) * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect) # Fill the cell
                pygame.draw.rect(screen, (0, 0, 0), rect, 1) # Draw a 1 pixel border


# Function to lock a tetromino in place
# This function takes the current tetromino, its position, and color

def lock_tetromino(shape, position, color):
    for row_index, row in enumerate(shape):
        for col_index, cell in enumerate(row):
            if cell:
                y = position[1] + row_index
                x = position[0] + col_index
                if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                    locked_grid[y][x] = color

# Function to check for collisions
def collision_with_locked_blocks():
    for row_index, row in enumerate(current_tetromino):
        for col_index, cell in enumerate(row):
            if cell:
                y = tetromino_position[1] + row_index
                x = tetromino_position[0] + col_index
                if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                    if locked_grid[y][x]:
                        return True
    return False

# Main game loop
def main():
    running = True
    last_fall_time = pygame.time.get_ticks()

    # Example Tetromino
    current_tetromino = SHAPES["I"][0]
    tetromino_position = [4, 0]
    tetromino_color = (128, 0, 128)

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    # Move left
                    if tetromino_position[0] > 0:
                        tetromino_position[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    # Move right
                    if tetromino_position[0] <= GRID_WIDTH - len(current_tetromino[0]):
                        tetromino_position[0] += 1
                elif event.key == pygame.K_DOWN:
                    # Move down
                    if tetromino_position[1] < GRID_HEIGHT - len(current_tetromino):
                        tetromino_position[1] += 1
    
        # Check if it's time for the tetromino to fall
        if current_time - last_fall_time > FALL_SPEED:
            # Move down
            if tetromino_position[1] < GRID_HEIGHT - len(current_tetromino):
                tetromino_position[1] += 1
            else:
                # Lock the Tetromino
                lock_tetromino(current_tetromino, tetromino_position, tetromino_color)
                # Spawn a new Tetromino
                current_tetromino = SHAPES['T']  # For now, just respawn the same shape
                tetromino_position = [4, 0]
            
            last_fall_time = current_time

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the grid
        draw_grid()

        # Draw the tetromino
        draw_tetromino(current_tetromino, tetromino_position, tetromino_color)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()