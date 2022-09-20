import pygame
class Ship:
    """A class to manage the ship"""
    def __init__(self,bs_game):
        """initialize the ship and its starting position"""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        #Load the ship image and get its get_rect
        self.image = pygame.image.load('C:/python_projects/space_ship.png')
        self.rect = self.image.get_rect()


        self.rect.midbottom = self.screen_rect.midbottom



    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
