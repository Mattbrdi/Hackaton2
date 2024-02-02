import pygame
import Monstre

class Personnage:

    def __init__(self, position,direction, life, gold) -> None:
        self._life = life #int
        self._position = position #tupple (line column)
        self._gold = gold #int
        self._direction = direction #string

    def get_position(self):
        return self._position

    def get_life(self):
        return self._life
    
    def get_gold(self):
        return self._gold

    def get_direction(self):    
        return self._direction
    
    def move(self):
        direction = self.get_direction
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
        return self

    def hurt(self, damage):
        return Personnage(self.get_position(), self.get_life()-damage)
    
    def heal(self, number):
        return Personnage(self.get_position, self.get_life()+number)

    def earn_gold(self, reward):
        return Personnage(self.get_position(), self.get_life(), self.get_gold()+reward)
    
    def draw(self, screen, l, color):
        rect = pygame.Rect(self.get_position[1]*l,self.get_position[0]*l , l, l)
        pygame.draw.rect(screen, color, rect)

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
        screen.blit(text_life, (50, 10)) # a changer

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


def process_events(direction, execute, perso):
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            execute = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            if event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            if event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
        
        if event.type == pygame.K_SPACE:
            perso.throw_arrow(direction, )

    return direction, execute

def draw_all(screen, l, perso_color, perso, list_arrow):
    draw_map()
    perso.draw(screen, l, perso_color)
    for arrow in list_arrow:
        arrow.draw(screen, l)

def move_all_arrows(list_of_arrows):
    list = []
    for arrow in list_of_arrows:
        arrow = arrow.make_move()
        if arrow is not None:
            list.append(arrow)
    return list

def update_display(screen, l, perso_color, perso, h, w):
    draw(h, w, screen, l)
    perso.get_score(screen)
    pygame.display.set_caption('Rogue GAME')
    pygame.display.update()