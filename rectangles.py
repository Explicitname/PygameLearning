import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
quitGame = False

while not quitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    
    pygame.display.flip()