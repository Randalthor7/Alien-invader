import pygame
import sys
import random
from settings import Settings


class Alien_Invasion:
    """Overall class for alien invasion"""


    def __init__ (self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Classy Invaders')
        icon = pygame.image.load('C:/python_projects/noclassship/ufo.png')
        pygame.display.set_icon(icon)
        self.playerimg = pygame.image.load('C:/python_projects/noclassship/fighter.png')
        self.enemyimg = pygame.image.load('C:/python_projects/noclassship/pixelated-alien.png')
        self.playerX = 370
        self.playerY = 480
        self.playerx_change = 0
        self.enemyX = random.randint(0,736)
        self.enemyY = random.randint(50,150)
        self.enemyX_change = 0.3
        self.enemyY_change = 40





    def _update_screen(self,Px,Py,Ex,Ey):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.enemyimg,(Ex,Ey))
        self.screen.blit(self.playerimg,(Px,Py))
        pygame.display.flip()


    def _change_x(self,Px):
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736

        self.playerX += self.playerx_change
        return self.playerX

    def _enemy_change(self,Ex,Ey):
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX_change = 0.3
            self.enemyY += self.enemyY_change
        elif self.enemyX >= 736:
            self.enemyX_change = -0.3
            self.enemyY += self.enemyY_change











    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.playerx_change = -0.3
                        print("left key has been pressed")
                    if event.key == pygame.K_RIGHT:
                        self.playerx_change = 0.3
                        print("right key has been pressed")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.playerx_change = 0






    def _run_game(self):
        while True:
            self._check_events()
            self._change_x(self.playerx_change)
            self._enemy_change(self,self.enemyX_change)
            self._update_screen(self.playerX,self.playerY,self.enemyX,self.enemyY)






ai = Alien_Invasion()
ai._run_game()
