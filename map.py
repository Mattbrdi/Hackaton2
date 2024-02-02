import pygame

class Map:
    def __init__(self, filename):
        self.map = []
        with open(filename, 'r') as file:
            for line in file:
                self.map.append(list(line)[:-1])
        
        self.map_decouverte = [[' ' for _ in range(len(row))] for row in self.map]
        print(self.map_decouverte)

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
    def update_map(self, x, y):
        self.map_decouverte = self.map   
"""
carte = Map('map.txt')
def draw(screen):     
    carte.update_map(0,0)  
    carte.draw_map(screen)
    

#-----------
pygame.init()
largeur, hauteur = 32*len(carte.map[0]), 32*len(carte.map)
taille_fenetre = (largeur, hauteur)
screen = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("screen")
couleur_fond = (0,0,0)
carte.update_map(0,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(couleur_fond)
    carte.draw_map(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(60)"""
