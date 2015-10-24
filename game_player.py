'''
Created on 23 okt. 2015

@author: danhe
'''

from game_tools import Sprite, world_to_graph, graph_to_world
from math import copysign, sqrt

class Player(Sprite):

    def __init__(self, id, position):
        super(Player, self).__init__(source='graphics/player.png')
        
        self.id = id
        
        self.size = (32, 32)
        
        self.position = position
        self.goal = self.position
        self.path = []
        self.pos = graph_to_world(self.position)
        self.new_pos = self.pos
        self.vel = (0, 0)
        
        return
    
    def on_touch_down(self, touch):
        
        if touch.button == 'left':
            self.goal = world_to_graph(touch.pos)
            
            self.path = self.parent.pathfinding(self.position, self.goal)
            
        return
    
    def update(self):
        
        if self.path and self.vel == (0, 0):
            
            node = self.path[0]
            del self.path[0]
            
            self.new_pos = graph_to_world(node)
            
            dx = node[0] - self.position[0]
            dy = node[1] - self.position[1]
            
            self.vel = (dx*4, dy*4)
        
        if copysign(1, self.vel[0])*(self.new_pos[0]-self.pos[0]) <= 0 and copysign(1, self.vel[1])*(self.new_pos[1]-self.pos[1]) <= 0:
            
            self.vel = (0, 0)
        
        self.pos[0] = round(self.pos[0] + self.vel[0])
        self.pos[1] = round(self.pos[1] + self.vel[1])
        self.position = world_to_graph(self.pos)
        
        return
    