import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake game")

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

snake = [(100,100),(90,100),(80,100)]
snake_dir = (CELL_SIZE,0)

#Food
def generate_food():
    while True:
         food_x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
         food_y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
         if (food_x, food_y) not in snake:
            return (food_x, food_y)

food = generate_food()

#Game variables
running = True
clock = pygame.time.Clock()
speed = 10
score = 0
level = 1
food_eaten = 0

# Font for displaying score and level
font = pygame.font.Font(None, 36)

while running:
    pygame.time.delay(100)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)
    
    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Check for wall collision
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False # End game if hit wall
    
    # Check for self-collision
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Check if food is eaten
    if new_head == food:
        food = generate_food()
        score += 10
        foods_eaten += 1
        
        # Level up system
        if foods_eaten % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()
    
    # Drawing section
    screen.fill(WHITE)
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Display score and level
    score_text = font.render(f"Score: {score}", True, BLUE)
    level_text = font.render(f"Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
