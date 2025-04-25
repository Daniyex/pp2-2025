import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")
clock = pygame.time.Clock()

radius = 5
mode = 'blue'  
drawing_mode = 'free'  
points = []
current_color = (0, 0, 255)
 

def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                drawing_mode = 'rect'
            elif event.key == pygame.K_c:
                drawing_mode = 'circle'
            elif event.key == pygame.K_e:
                drawing_mode = 'eraser'
                current_color = (0, 0, 0)
            elif event.key == pygame.K_f:
                drawing_mode = 'free'
                current_color = (0, 0, 255)  
            elif event.key == pygame.K_1:
                current_color = (0, 0, 255)   
            elif event.key == pygame.K_2:
                current_color = (255, 0, 0) 
            elif event.key == pygame.K_3:
                current_color = (0, 255, 0)  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                start_pos = event.pos
                if drawing_mode == 'free':
                    points.append(start_pos)
            elif event.button == 3:  
                radius = max(1, radius - 1)
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if drawing_mode == 'free':
                points.append(event.pos)
                points = points[-256:]
            elif drawing_mode == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing_mode in ['rect', 'circle'] and start_pos:
                end_pos = event.pos
                if drawing_mode == 'rect':
                    pygame.draw.rect(screen, current_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
                elif drawing_mode == 'circle':
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    pygame.draw.circle(screen, current_color, center, radius, 2)
                start_pos = None

    screen.fill((0, 0, 0))
    
    for i in range(len(points) - 1):
        drawLineBetween(screen, i, points[i], points[i + 1], radius, current_color)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()