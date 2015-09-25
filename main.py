from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.logger import Logger
from kivy.metrics import Metrics
from kivy.graphics import Color, Rectangle
from kivy.config import Config

import math

Config.set ( 'input', 'mouse', 'mouse,disable_multitouch' )

class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size

class Background(Widget):
    def __init__(self, source):
        super(Background, self).__init__()
        self.image = Sprite(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
    
    def update(self):
        return
    
    def on_touch_move(self, touch):
        
        if touch.button == 'right':
            self.image.x += touch.dsx*self.size[0]
            self.image.y += touch.dsy*self.size[1]

class Player(Sprite):
    def __init__(self, pos):
        super(Player, self).__init__(source='graphics/player.png', pos=pos)
        self.velocity_x = 0
        self.velocity_y = 0
        self.touch_x = pos[0]
        self.touch_y = pos[1]

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        if math.copysign(1, self.velocity_x)*(self.touch_x-self.x) < 0:
            self.velocity_x = 0
        
        if math.copysign(1, self.velocity_y)*(self.touch_y-self.y) < 0:
            self.velocity_y = 0

    def on_touch_down(self, touch):
        
        if touch.button == 'left':
            self.touch_x = touch.pos[0]
            self.touch_y = touch.pos[1]
            
            dx = self.x - self.touch_x
            dy = self.y - self.touch_y
            
            N = math.sqrt(dx**2 + dy**2)
            
            self.velocity_x = -2*dx/N
            self.velocity_y = -2*dy/N

class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        
        self.background = Background(source='graphics/map.png')
        self.size = self.background.size
        self.add_widget(self.background)
        self.player = Player(pos=[40,40])
        self.add_widget(self.player)
        Clock.schedule_interval(self.update, 1.0/60.0)
        
    def update(self, dt):
        self.background.update()
        self.player.update()
            
class GameApp(App):
    def build(self):
        game = Game()
        Window.size = [800,800]
        return game
    
if __name__ == "__main__":
        
        GameApp().run()