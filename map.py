import pygame


carre = 32
class Map:
    def __init__(self, filename):
        self.map = []
        with open(filename, 'r') as file:
            for line in file:
                self.map.append(list(line)[:-1])
        
        self.map_decouverte = [[' ' for _ in range(len(row))] for row in self.map]


    def draw_map(self, screen):
        for i in range(len(self.map_decouverte)):
            for j in range(len(self.map_decouverte[i])):
                if self.map_decouverte[i][j] == ' ':
                    pygame.draw.rect(screen, (0, 0, 0), (j*carre, i*carre, carre, carre))
                elif self.map_decouverte[i][j] == '.':
                    pygame.draw.rect(screen, (255,255,255), (j*carre, i*carre, carre, carre))
                elif self.map_decouverte[i][j] == '#':
                    pygame.draw.rect(screen, (100, 100, 100), (j*carre, i*carre, carre, carre))
                elif self.map_decouverte[i][j] == '+':
                    pygame.draw.rect(screen, (255, 255, 0), (j*carre, i*carre, carre, carre))
                elif self.map_decouverte[i][j] == '-' or self.map_decouverte[i][j] == '|': 
                    pygame.draw.rect(screen, (0, 0, 255), (j*carre, i*carre, carre, carre)) 
    def decouvre(self, x, y):
        self.map_decouverte[x][y] = self.map[x][y]   
    def cache(self, x, y):
        self.map_decouverte[x][y] = ' '



    
def point_with_caractere_next_to(carte, position, caractere):
    list_points = [position] 
    if carte.map[position[0]-1][position[1]] == caractere:
        list_points.append((position[0]-1, position[1]))
    if carte.map[position[0]+1][position[1]] == caractere :
        list_points.append((position[0]+1, position[1]))
    if carte.map[position[0]][position[1]-1] == caractere :
        list_points.append((position[0], position[1]-1))
    if carte.map[position[0]][position[1]+1] == caractere:
        list_points.append((position[0], position[1]+1))
    return list_points

def point_a_devoiler(carte, position): #position en (ligne, colonne)
    point_a_devoiler = []
    if carte.map[position[0]][position[1]] == '+':
        file = [(position[0], position[1])]
        while len(file)>0:
            for point in point_with_caractere_next_to(carte, file[0], '.'):
                if point not in point_a_devoiler and point not in file:
                    file.append(point)
            a= file.pop(0)
            point_a_devoiler.append(a)
                  
    else:
        point_a_devoiler.append((position[0]+1, position[1]))
        point_a_devoiler.append((position[0]-1, position[1]))
        point_a_devoiler.append((position[0], position[1]+1))
        point_a_devoiler.append((position[0], position[1]-1))
    return point_a_devoiler
  
def update_map(carte, perso):
    position = perso.get_position()
    for point in point_a_devoiler(carte, position):
        carte.decouvre(point[0], point[1])
        print(point)
def draw(screen, carte, perso):  
    update_map(carte, perso)  
    carte.draw_map(screen)

