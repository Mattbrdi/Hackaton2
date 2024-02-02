import pygame as pg

def norme_infini(x, y):
    return max(abs(x), abs(y))

def min(x,y):
    if abs(x) < abs(y):
        return x
    else:
        return y

class Monster:
    def __init__(self, name, health, damage, x, y, state, agro_reach, l, color):
        self.name = name 
        self.health = health 
        self.damage = damage 
        self.x = x
        self.y = y
        self.agro_reach = agro_reach
        self.size = l
        self.color = color
        self.state = state # 0 = alive, 1 = dead
    
    def is_legit_move(x, y, map):
        if map[x][y] == '|' or ' ' or '-':
            return False
        else:
            return True


    def move(self, Personnage, map):
        x = self.x
        y = self.y
        x_p = Personnage._position[0]
        y_p = Personnage._position[1]
        new_x = x
        new_y = y
        
        if norme_infini(x - x_p, y - y_p) <= self.agro_reach:
            if abs(x - x_p) >= abs(y - y_p):
                if x_p > x:
                    if self.is_legit_move(x + 1, y, map):
                        new_x += 1
                if x_p < x:
                    if self.is_legit_move(x - 1, y, map):
                        new_x -= 1
            else:
                
                if y_p > y:
                    if self.is_legit_move(x, y + 1, map):
                        new_y += 1
                if y_p < y:
                    if self.is_legit_move(x, y - 1, map):
                        new_y -= 1

        if new_x != x_p or new_y != y_p:
            map[new_x][new_y] = map[x][y]
            map[x][y] = '.'
            self.x = new_x
            self.y = new_y
        return (self.x, self.y)
    
    def attack(self, Personnage):
        x_p = Personnage._position[0]
        y_p = Personnage._position[1]
        x= self.x
        y= self.y
        if norme_infini(x - x_p, y - y_p) == 1 and (abs(x-x_p) -abs(y-y_p)) != 0:
            return self.damage
        else:
            return 0
    
    def take_damage(self, Arrows):
        for Arrow in Arrows:
            x = Arrow._position[0]
            y = Arrow._position[1]
            if x == self.x and y == self.y:
                self.health -= Arrow._damage

    def set_death(self):
        if self.health <= 0:
            self.state = 1

    def get_life(self):
        return self.health
    
    def get_position(self):
        return (self.x, self.y)

class Goblin(Monster):
    def __init__(self, name, health, damage, x, y, state, screen, l, color):
        super().__init__(name, health, damage, x, y, state, screen, l, color)

class JPG(Monster):
    def __init__(self, name, health, damage, x, y, state, screen, l, color):
        super().__init__(name, health, damage, x, y, state, screen, l, color)

class Collectibles:
    def __init__(self, name, x, y, screen, l, color):
        self.name = name
        self.x = x
        self.y = y
        self.screen = screen
        self.size = l
        self.color = color
        self.state = 0
    
    def draw(self):
        if self.state == 0:
            rect = pg.Rect(self.x*self.size, self.y*self.size, self.size, self.size)
            pg.draw.rect(self.screen, self.color, rect)

class Gold(Collectibles):
    def __init__(self, name, x, y, screen, l, color):
        super().__init__(name, x, y, screen, l, color)
    
    def is_collected(self, Personnage):
        x_p = Personnage._position[0]
        y_p = Personnage._position[1]
        if self.x == x_p and self.y == y_p:
            Personnage._gold += 10
            self.state = 1

class Potion(Collectibles):
    def __init__(self, name, x, y, screen, l, color):
        super().__init__(name, x, y, screen, l, color)
    
    def is_collected(self, Personnage):
        x_p = Personnage._position[0]
        y_p = Personnage._position[1]
        if self.x == x_p and self.y == y_p:
            Personnage._life += 100
            self.state = 1
        
def parse_monster_file(filename):
    monsters = {}
    with open(filename, 'r') as file:
        for line in file:
            # split the line at the equals sign
            parts = line.split('=')
            # strip whitespace and quotes from the monster name and number
            monster = parts[0].strip()
            number = parts[1].strip().replace("'", "")
            monsters[monster] = int(number)
    return monsters

