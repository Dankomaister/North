'''
Created on 2 okt. 2015

@author: danhe
'''

from kivy.uix.image import Image

class Sprite(Image):
    
    def __init__(self,**kwargs):
        
        super(Sprite,self).__init__(**kwargs)
        self.size = self.texture_size
        self.id = 'sprite'
        
        return
    