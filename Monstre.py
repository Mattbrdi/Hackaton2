import matplotlib.pyplot as plt
import pygame as pg
import time as t
import random as r
import sys
import player 
def norme_infini(x, y):
    return max(abs(x), abs(y))

def min(x,y):
    if abs(x) < abs(y):
        return x
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


    def move(self, x_p, y_p):
        x = self.x
        y = self.y
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
    
    def attack(self, x_p, y_p):
        x= self.x
        y= self.y
        if norme_infini(x - x_p, y - y_p) == 1 and (abs(x-x_p) -abs(y-y_p)) != 0:
            return self.damage
    
    def take_damage(self, player_damage):
        self.health -= player_damage

    def alive(self):
        if self.health <= 0:
            self.state = 1
    
    def draw(self):
        if self.state == 0:
            rect = pg.Rect(self.x*self.size, self.y*self.size, self.size, self.size)
            pg.draw.rect(self.screen, self.color, rect)
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
    
    def is_collected(self, x_p, y_p):
        if self.x == x_p and self.y == y_p:
            self.state = 1

class Potion(Collectibles):
    def __init__(self, name, x, y, screen, l, color):
        super().__init__(name, x, y, screen, l, color)
    
    def is_collected(self, x_p, y_p, player):
        if self.x == x_p and self.y == y_p:
            
            self.state = 1
        