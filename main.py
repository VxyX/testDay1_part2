import pygame

banyakRect = 500
# Initializing Pygame
pygame.init()
# clock = pygame.time.Clock()
 
# Initializing surface
max_width = 600
max_height = 400
screen = pygame.display.set_mode((max_width,max_height))

scroll_x = 0
scroll_y = 0

# Initializing Color
color = (0,0,255)

running = True


initX = 10
initY = 10
width = 50
height = 50
border = 2

created = 0

rect_surface = pygame.Surface((5000, 5000))
rect_surface.fill((255, 255, 255))
font = pygame.font.SysFont('Arial', 12)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Continuous scrolling based on mouse movement
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # Left mouse button pressed
                scroll_x += event.rel[0]
                # scroll_y += event.rel[1]
                
    if (created < banyakRect):
        for i in range(banyakRect):       
            pygame.draw.rect(rect_surface, color, (initX, initY, width, height), border)
            # method circle (surface, color, center_coor, radius, border)
            pygame.draw.circle(rect_surface, color, (initX + (width / 2), initY + (height / 2)), (width / 2) - (border), border)
            
            created += 1

            text_surface = font.render('{}'.format(created), True, color)
            rect_surface.blit(text_surface, (initX + (width / 2), initY + (height / 2)))

            initX += width
            print(created)

    screen.blit(rect_surface, (-scroll_x, -scroll_y))
    pygame.display.update()
# Drawing Rectangle
