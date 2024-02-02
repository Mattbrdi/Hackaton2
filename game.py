# The main algorithm of the game goes here
import pygame
from map import Map, draw
from perso import Personnage, update_display
import sys

class Game:
    def __init__(self):
        pass

    def run(self):
        """Run the game"""
        pygame.init()
        carte = Map('data/map.txt')
        perso = Personnage((2,2), 100, 0)
        largeur, hauteur = 32*len(carte.map[0]), 32*len(carte.map)
        taille_fenetre = (largeur, hauteur)
        screen = pygame.display.set_mode(taille_fenetre)
        pygame.display.set_caption("screen")
        couleur_fond = (0,0,0)

        while True:
            direction = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 'up'
                    if event.key == pygame.K_LEFT:
                        direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        direction = 'right'
                    if event.key == pygame.K_DOWN:
                        direction = 'down'

            perso = perso.make_move(carte.map, direction)
            screen.fill(couleur_fond)
            draw(carte, screen)
            update_display(screen, 32, (255, 0, 0), perso)
            pygame.display.flip()
            pygame.time.Clock().tick(20)
        