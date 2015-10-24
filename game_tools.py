'''
Created on 23 okt. 2015

@author: danhe
'''

from kivy.uix.image import Image
from math import floor

def graph_to_world(node):
    
    pos = (node[0]*32,node[1]*32)
    
    return pos

def world_to_graph(pos):
    
    node = (floor(pos[0]/32),floor(pos[1]/32))
    
    return node

class Sprite(Image):

    def __init__(self, **kwargs):
        super(Sprite,self).__init__(**kwargs)
        
        self.id = 'sprite'
        
        self.size = self.texture_size
        
        return