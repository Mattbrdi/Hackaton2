import matplotlib.pyplot as plt
import pygame as pg
import time as t
import random as r
import sys

def norme_infini(x, y):
    return max(abs(x), abs(y))


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
    
    def move(self, x, y, x_p, y_p):
        if norme_infini(x - x_p, y - y_p) <= self.agro_reach:
            if x < x_p:
                self.x += 1
            elif x > x_p:
                self.x -= 1
            if y < y_p:
                self.y += 1
            elif y > y_p:
                self.y -= 1
    
    def attack(self, x, y, x_p, y_p):
        if norme_infini(x - x_p, y - y_p) == 1:
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
     

        
    