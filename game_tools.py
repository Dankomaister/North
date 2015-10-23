'''
Created on 23 okt. 2015

@author: danhe
'''

from kivy.uix.image import Image

class Sprite(Image):

    def __init__(self, **kwargs):
        super(Sprite,self).__init__(**kwargs)
        
        self.id = 'sprite'
        
        self.size = self.texture_size
        
        return