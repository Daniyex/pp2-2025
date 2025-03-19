import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

mickey_bg = pygame.image.load(r"C:\Users\user\OneDrive\Desktop\PP2Labs\Lab7\clock.png")  
minute_hand = pygame.image.load(r"C:\Users\user\OneDrive\Desktop\PP2Labs\Lab7\rightarm.png")  
second_hand = pygame.image.load(r"C:\Users\user\OneDrive\Desktop\PP2Labs\Lab7\leftarm.png")  

mickey_bg = pygame.transform.scale(mickey_bg, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def rotate_hand(image, angle, center):
    """Rotate an image around a center point."""
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect.topleft

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(mickey_bg, (0, 0))  
    
    now = datetime.datetime.now()
    minute_angle = (now.minute % 60) * 6  
    second_angle = (now.second % 60) * 6  
    
    rotated_minute, minute_pos = rotate_hand(minute_hand, minute_angle, CENTER)
    rotated_second, second_pos = rotate_hand(second_hand, second_angle, CENTER)
    
    screen.blit(rotated_minute, minute_pos)
    screen.blit(rotated_second, second_pos)

    pygame.display.flip()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100) 

pygame.quit()
