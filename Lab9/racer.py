import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)

background = pygame.image.load(r"C:\Users\user\OneDrive\Desktop\PP2Labs\Lab9\background.jpg")  
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  



PLAYER_IMG = pygame.Surface((50, 100))
PLAYER_IMG = pygame.image.load(r"C:\Users\user\OneDrive\Desktop\PP2Labs\Lab9\car.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (100,50))  
PLAYER_IMG = pygame.transform.rotate(PLAYER_IMG, 90)  
ENEMY_IMG = pygame.Surface((50, 100))
ENEMY_IMG = pygame.image.load(r"C:\Users\user\OneDrive\Desktop\PP2Labs\Lab9\enemy.png")
ENEMY_IMG = pygame.transform.scale(ENEMY_IMG, (100,90))
ENEMY_IMG = pygame.transform.rotate(ENEMY_IMG,270)  

            
def draw_coin(weight):
    color = YELLOW if weight == 1 else (255, 165, 0)  
    surface = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.circle(surface, color, (15, 15), 15)
    return surface


clock = pygame.time.Clock()
FPS = 60

coin_spawn_delay = 60  
enemy_speed = 5
coin_collected = 0
speed_up_threshold = 5 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 120)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ENEMY_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), 0)

    def update(self):
        self.rect.move_ip(0, enemy_speed)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(50, WIDTH - 50)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2])  
        self.image = draw_coin(self.weight)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), 0)

    def update(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > HEIGHT:
            self.kill()

player = Player()
enemy = Enemy()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)


font = pygame.font.SysFont("Arial", 20)

running = True
frame_counter = 0
#global coin_collected()
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame_counter += 1
    if frame_counter >= coin_spawn_delay:
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)
        frame_counter = 0

    all_sprites.update()

    for coin in pygame.sprite.spritecollide(player, coins, True):
        coin_collected += coin.weight
        if coin_collected % speed_up_threshold == 0:
            enemy_speed += 1  

    if pygame.sprite.collide_rect(player, enemy):
        print("Game Over!")
        running = False

    all_sprites.draw(screen)

    score_text = font.render(f"Coins: {coin_collected}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
