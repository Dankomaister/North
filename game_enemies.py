'''
Created on 3 okt. 2015

@author: danhe
'''

from game_sprite import Sprite
from math import copysign, sqrt
from random import random

class Enemy1(Sprite):
    
    def __init__(self, id, position):
        super(Enemy1, self).__init__(source='graphics/enemy1.png', pos=position)
        self.id = id
        
        self.velocity = [0, 0]
        self.map_position = position
        self.map_offset = [0, 0]
                
        return
    
    def update(self):
        
        self.velocity[0] += 2*(0.5-random())
        self.velocity[1] += 2*(0.5-random())
        
        self.map_offset = self.parent.offset
        
        if not self.parent.collide_point(self.map_position[0],self.map_position[1]):
            self.map_position[0] -= self.velocity[0]
            self.map_position[1] -= self.velocity[1]
            self.velocity = [0,0]
        
        for child in self.parent.children:
            if child.id == self.id or child.id == 'sprite':
                continue
            if self.collide_widget(child):
                self.map_position[0] -= self.velocity[0]
                self.map_position[1] -= self.velocity[1]
                self.velocity = [0,0]
            print(self.id,child.id,self.collide_widget(child))
        
        self.map_position[0] += self.velocity[0]
        self.map_position[1] += self.velocity[1]
        self.x = self.map_position[0] + self.map_offset[0]
        self.y = self.map_position[1] + self.map_offset[1]
        
        return
    