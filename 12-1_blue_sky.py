import sys
import pygame
from settings import settings
from ship import Ship

class BlueSky:
    """overall class to manage blue sky"""
    def __init__(self):
        """initialize the game"""
        pygame.init()

        self.settings = settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Blue Sky")

        self.ship = Ship(self)

    def run_game(self):
        """start the main loop of the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(Self):
        #what for keyboard mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):

        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance run the game.
    bs = BlueSky()
    bs.run_game()
