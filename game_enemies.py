'''
Created on 3 okt. 2015

@author: danhe
'''

from game_sprite import Sprite
from math import copysign, sqrt
from random import random

class Enemy1(Sprite):
    
    def __init__(self, position):
        super(Enemy1, self).__init__(source='graphics/enemy1.png', pos=position)
        
        self.velocity = [0, 0]
        self.touch_position = position
        self.map_position = position
        self.map_offset = [0, 0]
                
        return
    
    def update(self,map):
        
        self.velocity[0] += 2*(0.5-random())
        self.velocity[1] += 2*(0.5-random())
        
        self.map_offset = map.offset
        self.map_position[0] += self.velocity[0]
        self.map_position[1] += self.velocity[1]
        
        if copysign(1, self.velocity[0]) * (self.touch_position[0] - self.map_position[0]) < 0:
            self.velocity[0] = 0
        
        if copysign(1, self.velocity[1]) * (self.touch_position[1] - self.map_position[1]) < 0:
            self.velocity[1] = 0
        
        if not map.collide_point(self.map_position[0],self.map_position[1]):
            self.map_position[0] -= self.velocity[0]
            self.map_position[1] -= self.velocity[1]
            self.velocity = [0,0]
        
        self.x = self.map_position[0] + self.map_offset[0]
        self.y = self.map_position[1] + self.map_offset[1]
        
        return
    