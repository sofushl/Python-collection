import pygame
import sys

# Constants
GRID_WIDTH = 15
GRID_HEIGHT = 10
CELL_SIZE = 40
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

opposite_direction = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}

class Snake:
    def __init__(self, start_pos, direction, color):
        self.body = [start_pos]
        self.direction = direction
        self.color = color
        self.next_direction = direction

    def get_head(self):
        return self.body[0]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Battle")
    clock = pygame.time.Clock()

    # Initialize snakes
    player_start = (0, 0)
    bot_start = (GRID_WIDTH - 1, GRID_HEIGHT - 1)
    player_snake = Snake(player_start, RIGHT, GREEN)
    bot_snake = Snake(bot_start, LEFT, RED)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Update player direction (prevent 180° turns)
                if event.key == pygame.K_UP and player_snake.direction != DOWN:
                    player_snake.next_direction = UP
                elif event.key == pygame.K_DOWN and player_snake.direction != UP:
                    player_snake.next_direction = DOWN
                elif event.key == pygame.K_LEFT and player_snake.direction != RIGHT:
                    player_snake.next_direction = LEFT
                elif event.key == pygame.K_RIGHT and player_snake.direction != LEFT:
                    player_snake.next_direction = RIGHT

        # Update directions
        player_snake.direction = player_snake.next_direction

        # Bot AI: Choose direction that minimizes distance to player
        player_head = player_snake.get_head()
        bot_head = bot_snake.get_head()
        all_bodies = player_snake.body + bot_snake.body

        valid_dirs = []
        for dir in [UP, DOWN, LEFT, RIGHT]:
            if dir != opposite_direction[bot_snake.direction]:
                new_head = (bot_head[0] + dir[0], bot_head[1] + dir[1])
                if 0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT:
                    if new_head not in all_bodies:
                        valid_dirs.append(dir)

        if valid_dirs:
            # Choose direction that minimizes Manhattan distance to player
            best_dir = min(
                valid_dirs,
                key=lambda d: abs(bot_head[0] + d[0] - player_head[0]) + 
                            abs(bot_head[1] + d[1] - player_head[1])
            )
            bot_snake.direction = best_dir

        # Move snakes
        for snake in [player_snake, bot_snake]:
            new_head = (snake.get_head()[0] + snake.direction[0],
                        snake.get_head()[1] + snake.direction[1])
            snake.body.insert(0, new_head)

        # Check collisions
        for snake in [player_snake, bot_snake]:
            head = snake.get_head()
            # Wall collision
            if not (0 <= head[0] < GRID_WIDTH and 0 <= head[1] < GRID_HEIGHT):
                game_over = True
            # Body collision
            if head in snake.body[1:] or head in (bot_snake.body if snake == player_snake else player_snake.body):
                game_over = True

        # Draw everything
        screen.fill(BLACK)
        
        # Draw grid
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1) 
        
        # Draw snakes
        for snake in [player_snake, bot_snake]:
            for segment in snake.body:
                pygame.draw.rect(screen, snake.color, 
                               (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    # Game over message
    font = pygame.font.Font(None, 74)
    text = font.render('GAME OVER', True, WHITE)
    screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()