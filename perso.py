import pygame
import Monstre

class Personnage:

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
        position = self.get_position()
        if direction == 'right':
            position = (position[0], position[1]+1)
            return Personnage(position, self.get_life(), self.get_gold())
        if direction == 'left':
            position = (position[0], position[1]-1)
            return Personnage(position, self.get_life(), self.get_gold())
        if direction == 'up':
            position = (position[0]-1, position[1])
            return Personnage(position, self.get_life(), self.get_gold())
        if direction == 'down':
            position = (position[0]+1, position[1])
            return Personnage(position, self.get_life(), self.get_gold())
        return self
    
    def is_legit_move(self, map, direction):
        futur_position = self.get_position()

        if direction == 'right':
            futur_position = (futur_position[0], futur_position[1]+1)
        if direction == 'left':
            futur_position = (futur_position[0], futur_position[1]-1)
        if direction == 'up':
            futur_position = (futur_position[0]-1, futur_position[1])
        if direction == 'down':
            futur_position = (futur_position[0]+1, futur_position[1])

        line = futur_position[0]
        column = futur_position[1]
        # check if line and column is within range
        if line < 0 or line >= len(map):
            return False
        if column < 0 or column >= len(map[0]):
            return False

        if map[line][column] == '.': #room
            return True
        elif map[line][column] == '|': #wall
            return False
        elif map[line][column] == '#': #corridor
            return True
        elif map[line][column] == ' ': #corridor wall
            return False

        elif map[line][column] == '+': #entry
            return True
        elif map[line][column] == '-': #wall
            return False
    

    def make_move(self, map, direction):
        if self.is_legit_move(map, direction):
            return self.move(direction)

        return self

    def hurt(self, damage):
        return Personnage(self.get_position(), self.get_life()-damage)
    
    def heal(self, number):
        return Personnage(self.get_position, self.get_life()+number)

    def earn_gold(self, reward):
        return Personnage(self.get_position(), self.get_life(), self.get_gold()+reward)
    
    def draw(self, screen, l, color):
        color = (255, 0, 0)
        rect = pygame.Surface((l, l))
        rect.fill(color)
        screen.blit(rect, (self.get_position()[1]*l,self.get_position()[0]*l))
        
    def throw_arrow(self, direction, list_of_arrow):
        position = self.get_position() #tupple
        direction = self.get_direction()
        list_of_arrow.append(Arrow(position, direction))

    def get_score(self, screen):
        police = pygame.font.Font(None, 36)
        yellow = (255, 255, 0)
        text_gold = police.render("Gold: {}".format(self.get_gold()), True, yellow)
        text_life = police.render("Life: {}".format(self.get_life()), True, yellow)
        screen.blit(text_gold, (10, 10))
        screen.blit(text_life, (100, 10))

class Arrow:

    def __init__(self, position, direction, damage) -> None:
        self._direction = direction
        self._position = position
        self._damage = damage

    def get_damage(self):
        return self._damage
    
    def get_position(self):
        return self._position

    def get_direction(self):    
        return self._direction

    def move(self):
        direction = self.get_direction()
        position = self.get_position()
        damage = self.get_damage()
        if direction == 'right':
            position = (position[0], position[1]+1)
            return Arrow(position, direction)
        if direction == 'left':
            position = (position[0], position[1]-1)
            return Arrow(position, direction)
        if direction == 'up':
            position = (position[0]-1, position[1]+1)
            return Arrow(position, direction)
        if direction == 'down':
            position = (position[0]+1, position[1]+1)
            return Arrow(position, direction)

    def is_legit_move(self, map, move):
        direction = self.get_direction()
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
        elif map[line][column] == '+': #entry
            return True
        elif map[line][column] == '-': #wall
            return False
    
    def make_move(self, map, move):
        direction = self
        if self.is_legit_move():
            return move(self, direction)
        return None
    
    def draw(self, screen, l):
        l_arrow = l/3
        black = (255, 255, 255)
        rect = pygame.Rect(self.get_position[1]*l_arrow+l_arrow,self.get_position[0]*l_arrow+l_arrow , l_arrow, l_arrow)
        pygame.draw.rect(screen, black, rect)

    def meet_monster(self, monsters):
        for monster in monsters:
            if monster.get_position() == self.get_position():
                return None #we met a monster
        return self #we did not met a monster

def update_display(screen, l, perso_color, perso):
    perso.get_score(screen)
    perso.draw(screen, l, perso_color)
    pygame.display.set_caption('Rogue GAME')
    pygame.display.update()