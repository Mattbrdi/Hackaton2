import matplotlib.pyplot as plt
import pygame as pg
import time as t
import random as r

def norme_infini(x, y):
    return max(abs(x), abs(y))

def min(x,y):
    if abs(x) < abs(y):
        return x
    else:
        return y

class Monster:
    def __init__(self, name, health, damage, x, y, state, screen, agro_reach, l, color):
        self.name = name 
        self.health = health 
        self.damage = damage 
        self.x = x
        self.y = y
        self.screen = screen 
        self.agro_reach = agro_reach
        self.size = l
        self.color = color
        self.state = state # 0 = alive, 1 = dead
    
    def is_legit_move(x,y, map):
        if map[x][y] == '|' or ' ' or '-':
            return False
        else:
            return True


    def move(self, Personnage):
        x = self.x
        y = self.y
        x_p = Personnage._position[0]
        y_p = Personnage._position[1]
        if norme_infini(x - x_p, y - y_p) <= self.agro_reach:
            if min(x-x_p, y-y_p) == (x-x_p):
                if x < x_p:
                    if self.is_legit_move(x+1, y, map):
                        self.x += 1
                elif x > x_p:
                    if self.is_legit_move(x-1, y, map):
                        self.x -= 1
            else : 
                if y < y_p:
                    if self.is_legit_move(x, y+1, map):
                        self.y += 1
                elif y > y_p:
                    if self.is_legit_move(x, y-1, map):
                        self.y -= 1
    
    def attack(self, Personnage):
        x_p = Personnage._position[0]
        y_p = Personnage._position[1]
        x= self.x
        y= self.y
        if norme_infini(x - x_p, y - y_p) == 1 and (abs(x-x_p) -abs(y-y_p)) != 0:
            return self.damage
    
    def take_damage(self, Arrow):
        for Arrow in Arrows:
            x = Arrow._position[0]
            y = Arrow._position[1]
            if x == self.x and y == self.y:
                player_damage = Arrow._damage
                self.health -= player_damage

    def alive(self):
        if self.health <= 0:
            self.state = 1
    
    def draw(self):
        if self.state == 0:
            rect = pg.Rect(self.x*self.size, self.y*self.size, self.size, self.size)
            pg.draw.rect(self.screen, self.color, rect)
    
    def get_position(self):
        return (self.x, self.y)
    '''
class Goblin(Monster):
    def __init__(self, name, health, damage, x, y, state, screen, l, color):
        super().__init__(name, health, damage, x, y, state, screen, l, color)

class JPG(Monster):
    def __init__(self, name, health, damage, x, y, state, screen, l, color):
        super().__init__(name, health, damage, x, y, state, screen, l, color)
    '''

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

