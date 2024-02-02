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
    
    def make_move(self, map, move, direction):
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

    def attack(): #TODO
        pass

    def get_score(self, screen):
        police = pygame.font.Font(None, 36)
        yellow = (255, 255, 0)
        text_gold = police.render("Gold: {}".format(self.get_gold()), True, yellow)
        text_life = police.render("Life: {}".format(self.get_life()), True, yellow)
        screen.blit(text_gold, (10, 10))
        screen.blit(text_life, (50, 10))


def process_events(direction, execute):
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
    return direction, execute

def draw(screen, l, perso_color, perso):
    draw_map()
    perso.draw(screen, l, perso_color)

def update_display(screen, l, perso_color, perso, h, w):
    draw(h, w, screen, l)
    perso.get_score(screen)
    pygame.display.set_caption('Rogue GAME')
    pygame.display.update()