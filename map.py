import pygame
import random
from Monstre import Goblin, JPG


class Map:
    def __init__(self, filename):
        self.map = []
        with open(filename, 'r') as file:
            for line in file:
                self.map.append(list(line)[:-1])
    
        accessibleCoordinates = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '.':
                    accessibleCoordinates.append((i, j))

        random.shuffle(accessibleCoordinates)
        for i in range(7):
            x, y = accessibleCoordinates.pop()
            self.map[x][y] = Goblin('goblin', 100, 10, x, y, 0, 5, 32, (0, 255, 0))
        for i in range(7):
            x, y = accessibleCoordinates.pop()
            self.map[x][y] = JPG('jpg', 100, 10, x, y, 0, 5, 32, (255, 0, 0))
        
        self.map_decouverte = [[' ' for _ in range(len(row))] for row in self.map]

    def draw_map(self, screen):
        for i in range(len(self.map_decouverte)):
            for j in range(len(self.map_decouverte[i])):
                if self.map_decouverte[i][j] == ' ':
                    pygame.draw.rect(screen, (0, 0, 0), (j*32, i*32, 32, 32))
                elif self.map_decouverte[i][j] == '.':
                    pygame.draw.rect(screen, (255,255,255), (j*32, i*32, 32, 32))
                elif self.map_decouverte[i][j] == '#':
                    pygame.draw.rect(screen, (100, 100, 100), (j*32, i*32, 32, 32))
                elif self.map_decouverte[i][j] == '+':
                    pygame.draw.rect(screen, (255, 255, 0), (j*32, i*32, 32, 32))
                elif self.map_decouverte[i][j] == '-' or self.map_decouverte[i][j] == '|': 
                    pygame.draw.rect(screen, (0, 0, 255), (j*32, i*32, 32, 32))
                elif isinstance(self.map[i][j], Goblin):
                    image = pygame.image.load('images/goblin.jpeg')
                    image = pygame.transform.scale(image, (32, 32))
                    screen.blit(image, (j*32, i*32))
                elif isinstance(self.map[i][j], JPG):
                    image = pygame.image.load('images/demon.jpeg')
                    image = pygame.transform.scale(image, (32, 32))
                    screen.blit(image, (j*32, i*32))
        
    def decouvre(self, x, y):
        self.map_decouverte = self.map   

def draw(carte, screen):     
    carte.decouvre(0,0)  
    carte.draw_map(screen)
