import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
quitGame = False
isBlue = False

while not quitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            isBlue = not isBlue
            
    if isBlue: 
        color = (0, 128, 255)
    else: 
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    
    pygame.display.flip()