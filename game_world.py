'''
Created on 23 okt. 2015

@author: danhe
'''

from kivy.uix.widget import Widget

class GameWorld(Widget):

    def __init__(self):
        super(GameWorld,self).__init__()
        
        self.id = 'gameworld'
        
        return
    
    def update(self):
        
        for child in self.children:
            child.update()
        
        return
    