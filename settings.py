import json
import os
import pygame

# Loads the settings from the data/settings.json file

class Settings:
    """A class to store all settings for Rogue"""
    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.caption = "Rogue"
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.caption)
        self.settings_file = "data/settings.json"
        self.load_settings()
        
    def load_settings(self):
        """Load the settings from the settings file"""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                settings = json.load(f)
                self.screen_width = settings['screen_width']
                self.screen_height = settings['screen_height']
                self.bg_color = settings['bg_color']
                self.caption = settings['caption']
                self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                pygame.display.set_caption(self.caption)
        else:
            self.save_settings()
    
    def save_settings(self):
        """Save the settings to the settings file"""
        settings = {
            'screen_width': self.screen_width,
            'screen_height': self.screen_height,
            'bg_color': self.bg_color,
            'caption': self.caption
        }
        with open(self.settings_file, 'w') as f:
            json.dump(settings, f)
            
    def set_screen(self, screen_width, screen_height):
        """Set the screen size"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.save_settings()
        
    def set_bg_color(self, bg_color):
        """Set the background color"""
        self.bg_color = bg_color
        self.save_settings()
        
    def set_caption(self, caption):
        """Set the caption"""
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.save_settings()

    def set_username(self, username):
        """Set the username"""
        self.username = username
        self.save_settings()
        
    def get_screen(self):
        """Get the screen"""
        return self.screen
    
    def get_bg_color(self):
        """Get the background color"""
        return self.bg_color
    
    def get_caption(self):
        """Get the caption"""
        return self.caption