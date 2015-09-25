from kivy.app import App
from kivy.uix.widget import Widget
#------------------------------------ from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image

class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size

class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.background = Sprite(source='images/a.png')
        self.size = self.background.size
        self.add_widget(self.background)
        self.add_widget(Sprite(source='images/a1.png'))
    #--------------------------------------------- def __init__(self, **kwargs):
        #---------------------------------- super(Game, self).__init__(**kwargs)
        #----------------------------------------------------- with self.canvas:
            #------------------------------------------------ Color(.5, .5, 1.0)
            #------------------------------ Rectangle(pos=(0,0), size=self.size)
            #-------------------------------------------------------------- pass
    #------------------------------------------------------- def __init__(self):
        #------------------------------------------ super(Game, self).__init__()
        #------------------------ self.add_widget(Sprite(source='images/a.png'))
            
class GameApp(App):
    def build(self):
        #----------------------------------------- return Game(size=Window.size)
        #--------------------------------------------------------- return Game()
        game = Game()
        Window.size = game.size
        return game
    
if __name__ == "__main__":
        
        GameApp().run()