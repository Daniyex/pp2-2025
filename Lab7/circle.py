import pygame
import sys

pygame.init()


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_RADIUS = 25
MOVE_STEP = 20
BALL_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Red Ball Movement")

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BG_COLOR)

    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - MOVE_STEP - BALL_RADIUS >= 0:
                y -= MOVE_STEP
            elif event.key == pygame.K_DOWN and y + MOVE_STEP + BALL_RADIUS <= SCREEN_HEIGHT:
                y += MOVE_STEP
            elif event.key == pygame.K_LEFT and x - MOVE_STEP - BALL_RADIUS >= 0:
                x -= MOVE_STEP
            elif event.key == pygame.K_RIGHT and x + MOVE_STEP + BALL_RADIUS <= SCREEN_WIDTH:
                x += MOVE_STEP

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
