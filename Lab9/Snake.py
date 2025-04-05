import pygame
import random
import time
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 10

font = pygame.font.SysFont("Arial", 20)

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.dx, self.dy = 1, 0  
        self.grow_flag = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.dx, head[1] + self.dy)
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.dx, -self.dy):  
            self.dx, self.dy = dx, dy

    def grow(self):
        self.grow_flag = True

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def collides_with_wall(self):
        x, y = self.body[0]
        return x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = self.random_position()
        self.weight = random.choice([1, 2, 3])  
        self.spawn_time = time.time()

    def random_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def is_expired(self):
        return time.time() - self.spawn_time > 5  

    def draw(self):
        color = RED if self.weight == 1 else YELLOW if self.weight == 2 else WHITE
        pygame.draw.rect(screen, color, (self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    snake = Snake()
    food = Food()
    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.change_direction(0, -1)
        elif keys[pygame.K_DOWN]:
            snake.change_direction(0, 1)
        elif keys[pygame.K_LEFT]:
            snake.change_direction(-1, 0)
        elif keys[pygame.K_RIGHT]:
            snake.change_direction(1, 0)

        snake.move()

        if snake.body[0] == food.position:
            score += food.weight
            snake.grow()
            food = Food()  

        if food.is_expired():
            food = Food()

        if snake.collides_with_self() or snake.collides_with_wall():
            print("Game Over! Final Score:", score)
            running = False

        snake.draw()
        food.draw()
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
