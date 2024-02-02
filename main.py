# Create a main menu for the game rogue using pygame
# It should have 3 buttons, start, options, and quit
# Options should save user settings to a json file

import pygame
import sys
import json
import os
from button import Button
from settings import Settings
from game import Game

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rogue")

# Set up the settings
settings = Settings()

# Display background image
background = pygame.image.load("images/main_menu.jpeg")
# background = pygame.transform.scale(background, (800, 600))
screen.blit(background, (-50, 0))

# Display title
font = pygame.font.SysFont("Georgia", 100)
text = font.render("Rogue", True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.center = (400, 100)
screen.blit(text, text_rect)

# Set up the buttons
start_button = Button(60, 300, 200, 50, "Start", font="Georgia")
options_button = Button(60, 400, 200, 50, "Options", font="Georgia")
quit_button = Button(60, 500, 200, 50, "Quit", font="Georgia")

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if start_button.is_clicked(x, y):
                game = Game(settings)
                game.run()
            elif options_button.is_clicked(x, y):
                settings.save_settings()
            elif quit_button.is_clicked(x, y):
                sys.exit()
    
    # Draw the buttons
    start_button.draw(screen)
    options_button.draw(screen)
    quit_button.draw(screen)
    
    # Update the screen
    pygame.display.flip()

