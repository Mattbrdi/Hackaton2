from perso import Personnage
import pygame

class Bomb:
    
    def __init__(self, position, damage, range) -> None:
        self._position = position #tupple (line, column)
        self._range = range #int
        self._damage = damage #int

    def get_position(self):
        return self._position

    def draw_bomb(self):
        pass

    def draw_explosion(self, screen): #every in range case turns orange for a frame

        color = (255, 0, 0)
        rect = pygame.Surface((l, l))
        rect.fill(color)
        screen.blit(rect, (self.get_position()[1]*l,self.get_position()[0]*l))

    def get_list_range(self):
        list_range = [(self.get_position())]

        for l in range(self._position[0] - self._range, self._position[0] - self._range+1):
            for c in range(self._position[1] - self._range, self._position[1] - self._range+1):
                list_range.append((l, c))
        return list_range

    def kill(self, list_monster, perso):
        list_range = self.get_list_range()
        if perso.get_position() in list_range:
            perso = perso.hurt(self._damage)
        for monster in list_monster:
            if monster.get_position() in list_range:
                pass # TODO kill monster
    
        return perso, list_monster