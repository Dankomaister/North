from kivy.app import App
from kivy.uix.widget import Widget
#------------------------------------ from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock

class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size

# class Background(Sprite):
#     def update(self):
#         self.x -= 2
class Background(Widget):
    def __init__(self, source):
        super(Background, self).__init__()
        self.image = Sprite(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source=source, x=self.width)
        self.add_widget(self.image_dupe)
        
#     def update(self):
#         self.image.x -= 1 * params.scale
#         self.image_dupe.x -= 1 * params.scale
    def update(self):
        self.image.x -= 2
        self.image_dupe.x -= 2        
        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width


class Player(Sprite):
    def __init__(self, pos):
#         self.images = SpriteAtlas('images/bird_anim.atlas')
        super(Player, self).__init__(source='graphics/player.png', pos=pos)
        self.velocity_y = 0
        self.gravity = -.1 
        
    def update(self):
        self.velocity_y += self.gravity
        self.velocity_y = max(self.velocity_y, -10)
        self.y += self.velocity_y
#         if self.velocity_y < -5 * params.scale:
#             self.texture = self.images['wing-up']
#         elif self.velocity_y < 0:
#             self.texture = self.images['wing-mid']

    def on_touch_down(self, *ignore):
        self.velocity_y = 5.5 
#         self.texture = self.images['wing-down']
#         sfx_flap.play()





class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
#         self.background = Sprite(source='images/a.png')
        self.background = Background(source='graphics/map1.png')
        self.size = self.background.size
        self.add_widget(self.background)
#         self.add_widget(Sprite(source='graphics/player.png'))
        self.player = Player(pos=(0, self.height / 2))
        self.add_widget(self.player)

    #--------------------------------------------- def __init__(self, **kwargs):
        #---------------------------------- super(Game, self).__init__(**kwargs)
        #----------------------------------------------------- with self.canvas:
            #------------------------------------------------ Color(.5, .5, 1.0)
            #------------------------------ Rectangle(pos=(0,0), size=self.size)
            #-------------------------------------------------------------- pass
    #------------------------------------------------------- def __init__(self):
        #------------------------------------------ super(Game, self).__init__()
        #------------------------ self.add_widget(Sprite(source='images/a.png'))
        
        Clock.schedule_interval(self.update, 1.0/60.0)
        
    def update(self, *ignore):
        self.background.update()
        self.player.update()
            
class GameApp(App):
    def build(self):
        #----------------------------------------- return Game(size=Window.size)
        #--------------------------------------------------------- return Game()
        game = Game()
        Window.size = [600,600]
        return game
    
if __name__ == "__main__":
        
        GameApp().run()