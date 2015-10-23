'''
Created on 23 okt. 2015

@author: danhe
'''

from game_sprite import Sprite

class Map(Sprite):

    def __init__(self, map_file):
        super(Map,self).__init__(source=map_file)
        
        self.id = 'map'
        
        return
    