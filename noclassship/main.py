import pygame

#Intialize the pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('C:/python_projects/noclassship/ufo.png')
pygame.display.set_icon(icon)


#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
s
