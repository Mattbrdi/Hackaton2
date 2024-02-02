import pygame

class Personnage():

    def __init__(self, position, life, gold) -> None:
        self._life = life #int
        self._position = position #tupple (line column)
        self._gold = gold #int

    def get_position(self):
        return self._position

    def get_life(self):
        return self._life
    
    def get_gold(self):
        return self._gold

    def move(self, direction):
        if direction == 'right':
            position = (position[0], position[1]+1)
            return Personnage(position, self.get_life(), self.get_gold())
        if direction == 'left':
            position = (position[0], position[1]-1)
            return Personnage(position, self.get_life(), self.get_gold())
        if direction == 'up':
            position = (position[0]-1, position[1]+1)
            return Personnage(position, self.get_life(), self.get_gold())
        if direction == 'down':
            position = (position[0]+1, position[1]+1)
            return Personnage(position, self.get_life(), self.get_gold())
    
    def is_legit_move(self, map, move, direction):
        futur_position = move(self, direction).get_position()
        line = futur_position[0]
        column = futur_position[1]
        if map[line][column] == '.': #room
            return True
        elif map[line][column] == '|': #wall
            return False
        elif map[line][column] == '#': #corridor
            return True
        elif map[line][column] == ' ': #corridor wall
            return False
        elif map[line][column] == '+':
            return True
        elif map[line][column] == '-':
            return False
        
    def hurt(self, damage):
        return Personnage(self.get_position(), self.get_life()-damage)
    
    def heal(self, number):
        return Personnage(self.get_position, self.get_life()+number)

    def earn_gold(self):
        return Personnage(self.get_position(), self.get_life(), self.get_gold()+1)
    
    def draw(self, screen, l, color):
        rect = pygame.Rect(self.get_position[1]*l,self.get_position[0]*l , l, l)
        pygame.draw.rect(screen, color, rect)

    

    
        