import pygame
pygame.init()
scr = pygame.display.set_mode((600,400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

#Make all the asset objects here

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #Display all the assets here
    pygame.display.update()
    clock.tick(60)