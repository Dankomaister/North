'''
Created on 2 okt. 2015

@author: danhe
'''

from game_sprite import Sprite
from math import copysign, sqrt

class Player(Sprite):
    
    def __init__(self, id, position):
        super(Player, self).__init__(source='graphics/player.png', pos=position)
        self.id = id
        
        self.velocity = [0, 0]
        self.touch_position = position
        self.map_position = position
        self.map_offset = [0, 0]
        
        return
    
    def update(self):
        
        print(self.children)
        
        self.map_offset = self.parent.offset
        
        if copysign(1, self.velocity[0]) * (self.touch_position[0] - self.map_position[0]) < 0:
            self.velocity[0] = 0
        
        if copysign(1, self.velocity[1]) * (self.touch_position[1] - self.map_position[1]) < 0:
            self.velocity[1] = 0
        
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
        
#         print(self.parent.children[0].map_position)
#         print(self.collide_widget(self.parent.children[0]))
        
        return
    
    def on_touch_down(self, touch):
        
        if touch.button == 'left':
            self.touch_position = list(touch.pos)
            self.touch_position[0] -= self.map_offset[0]
            self.touch_position[1] -= self.map_offset[1]
            
            dx = self.map_position[0] - self.touch_position[0]
            dy = self.map_position[1] - self.touch_position[1]
            
            N = sqrt(dx ** 2 + dy ** 2)
            
            self.velocity[0] = -5 * dx / N
            self.velocity[1] = -5 * dy / N
        
        return
    
