# The main algorithm of the game goes here
import pygame

class Game:
    def __init__(self, settings):
        """Initialize the game"""
        self.settings = settings
        self.screen = settings.screen
        self.bg_color = settings.bg_color
        self.caption = settings.caption
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        self.username = settings.username
        self.running = True

    def run(self):
        """Run the game"""
        pygame.display.set_caption(self.caption)
        while self.running:
            self._check_events()
            self._update_screen()
        