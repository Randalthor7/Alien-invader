import pygame
import random

#Intialize the pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load('C:/python_projects/noclassship/space_background.png')


#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('C:/python_projects/noclassship/ufo.png')
pygame.display.set_icon(icon)

#Player
playerimg = pygame.image.load('C:/python_projects/noclassship/fighter.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyimg = pygame.image.load('C:/python_projects/noclassship/pixelated-alien.png')
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40


def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y):
    screen.blit(enemyimg,(x,y))
#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether ts left of right.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is being pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                print("right key is being pressed")
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("Keystroke has been released")

    #Background image
    screen.blit(background,(0,0))

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
