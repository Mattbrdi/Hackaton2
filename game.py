# The main algorithm of the game goes here
import pygame
from map import Map, draw
from perso import Personnage, update_display
from Monstre import Goblin, JPG
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
        last_direction = 'right'
        list_arrow = []

        running = True
        while running:
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
                    if direction is not None:
                        last_direction = direction
                    if event.key == pygame.K_SPACE:
                        perso.throw_arrow(last_direction, list_arrow)

            for i in range(len(carte.map)):
                for j in range(len(carte.map[i])):
                    if isinstance(carte.map[i][j], (Goblin, JPG)):
                        perso = perso.hurt(carte.map[i][j].attack(perso))
                        carte.map[i][j].take_damage(list_arrow)
                        if (carte.map[i][j].get_life() <= 0):
                            carte.map[i][j].set_death()
                            carte.map[i][j] = '.'
                            perso = perso.earn_gold(10)
            
            perso = perso.make_move(carte.map, direction)
            screen.fill(couleur_fond)
            draw(carte, screen)
            update_display(screen, 32, (255, 0, 0), perso)
           
            new_list_arrow = []
            for arrow in list_arrow:
                x, y = arrow.get_position()
                if isinstance(carte.map[x][y], (Goblin, JPG)):
                    continue
                if arrow.is_legit_move(carte.map):
                    new_list_arrow.append(arrow.move())
            list_arrow = new_list_arrow

            for arrow in list_arrow:
                arrow.draw(screen, 32)
            
            """
            if perso.get_life() <= 0:
                images = pygame.image.load('images/game_over.jpeg')
                screen.blit(images, (-60,0))
                running = False
            """

            pygame.display.flip()
            pygame.time.Clock().tick(20)
        