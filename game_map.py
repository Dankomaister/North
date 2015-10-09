'''
Created on 2 okt. 2015

@author: danhe
'''

from kivy.uix.widget import Widget
from game_sprite import Sprite

class World(Widget):
    
    def __init__(self,map_file):
        super(World,self).__init__()
        
        self.sprite = Sprite(source=map_file)
        self.size = self.sprite.size
        self.offset = [0,0]
        
        self.id = 'test'
        
        self.add_widget(self.sprite)
        
        return
    
    def update(self):
        
        self.sprite.x = self.offset[0]
        self.sprite.y = self.offset[1]
        
        for child in self.children:
            if child.id == 'sprite':
                continue
            child.update()
    
    def on_touch_move(self, touch):
        
        if touch.button == 'right':
            self.offset[0] += touch.dsx*self.size[0]
            self.offset[1] += touch.dsy*self.size[1]
        
        return
    