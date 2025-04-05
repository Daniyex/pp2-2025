import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Shapes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)


clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

drawing = False
start_pos = None
shape = "square"  
shapes = []  

def draw_right_triangle(surf, start, end):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(surf, BLUE, [start, (x1, y2), end], 2)

def draw_equilateral_triangle(surf, start, end):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    top = (x1, y1)
    left = (x1 - side // 2, y1 + int(side * math.sqrt(3) / 2))
    right = (x1 + side // 2, y1 + int(side * math.sqrt(3) / 2))
    pygame.draw.polygon(surf, BLUE, [top, left, right], 2)

def draw_rhombus(surf, start, end):
    x1, y1 = start
    x2, y2 = end
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    half_width = abs(x2 - x1) // 2
    half_height = abs(y2 - y1) // 2
    points = [
        (center_x, y1),  
        (x2, center_y),  
        (center_x, y2),  
        (x1, center_y)    
    ]
    pygame.draw.polygon(surf, BLUE, points, 2)

def draw_saved_shapes():
    for shape_data in shapes:
        kind, start, end = shape_data
        if kind == "square":
            draw_square(screen, start, end)
        elif kind == "right":
            draw_right_triangle(screen, start, end)
        elif kind == "equilateral":
            draw_equilateral_triangle(screen, start, end)
        elif kind == "rhombus":
            draw_rhombus(screen, start, end)

def draw_square(surf, start, end):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(surf, BLUE, rect, 2)

def draw_ui():
    shape_text = font.render(f"Shape: {shape.capitalize()}", True, BLACK)
    screen.blit(shape_text, (10, 10))
    info_text = font.render("Keys: 1-Square 2-Right 3-Equilateral 4-Rhombus | ESC to Quit", True, BLACK)
    screen.blit(info_text, (10, HEIGHT - 30))

running = True
while running:
    screen.fill(WHITE)
    draw_saved_shapes()
    draw_ui()

    if drawing and start_pos:
        if shape == "square":
            draw_square(screen, start_pos, pygame.mouse.get_pos())
        elif shape == "right":
            draw_right_triangle(screen, start_pos, pygame.mouse.get_pos())
        elif shape == "equilateral":
            draw_equilateral_triangle(screen, start_pos, pygame.mouse.get_pos())
        elif shape == "rhombus":
            draw_rhombus(screen, start_pos, pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            shapes.append((shape, start_pos, end_pos))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_1:
                shape = "square"
            elif event.key == pygame.K_2:
                shape = "right"
            elif event.key == pygame.K_3:
                shape = "equilateral"
            elif event.key == pygame.K_4:
                shape = "rhombus"

    pygame.display.update()
    clock.tick(60)

pygame.quit()

#Controls
#Key	Shape
#1	Square
#2	Right Triangle
#3	Equilateral Triangle
#4	Rhombus
#ESC	Quit Game