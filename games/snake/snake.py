import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Game window settings
WIDTH = 800
HEIGHT = 800
BLOCK_SIZE = 40
SPEED = 6

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Snake initialization
def init_snake():
    return [
        [WIDTH // 2, HEIGHT // 2],
        [WIDTH // 2 - BLOCK_SIZE, HEIGHT // 2],
        [WIDTH // 2 - 2 * BLOCK_SIZE, HEIGHT // 2]
    ]

# Game functions
def show_score(score):
    font = pygame.font.SysFont(None, 35)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

def game_over():
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over!", True, RED)
    screen.blit(text, [WIDTH//2 - 140, HEIGHT//2 - 40])
    font = pygame.font.SysFont(None, 50)
    text = font.render("Press SPACE to restart", True, WHITE)
    screen.blit(text, [WIDTH//2 - 160, HEIGHT//2 + 20])
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

def main():
    snake = init_snake()
    direction = 'RIGHT'
    next_dir = direction
    food = [
        random.randrange(BLOCK_SIZE, WIDTH - BLOCK_SIZE, BLOCK_SIZE),
        random.randrange(BLOCK_SIZE, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    ]
    score = 0
    game_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    next_dir = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    next_dir = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    next_dir = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    next_dir = 'RIGHT'


        if game_active:
            # Update direction
            direction = next_dir

            # Move snake
            head = [snake[0][0], snake[0][1]]
            if direction == 'UP':
                head[1] -= BLOCK_SIZE
            elif direction == 'DOWN':
                head[1] += BLOCK_SIZE
            elif direction == 'LEFT':
                head[0] -= BLOCK_SIZE
            elif direction == 'RIGHT':
                head[0] += BLOCK_SIZE

            # Check collisions
            if (head[0] < 0 or head[0] >= WIDTH or
                head[1] < 0 or head[1] >= HEIGHT or
                head in snake):
                game_active = False
                game_over()
                return

            snake.insert(0, head)

            # Check food collision
            if head == food:
                score += 1
                food = [
                    random.randrange(0, WIDTH, BLOCK_SIZE),
                    random.randrange(0, HEIGHT, BLOCK_SIZE)
                ]
                # Ensure food doesn't spawn on snake
                while food in snake:
                    food = [
                        random.randrange(0, WIDTH, BLOCK_SIZE),
                        random.randrange(0, HEIGHT, BLOCK_SIZE)
                    ]
            else:
                snake.pop()

            # Draw everything
            screen.fill(BLACK)
            for pos in snake:
                pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
            show_score(score)
            pygame.display.flip()
            clock.tick(SPEED)

if __name__ == "__main__":
    main()