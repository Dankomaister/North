
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *

class MyWidget(Widget):
    
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()
        
        return
    
    def update_canvas(self, *args):
        self.canvas.clear()
        self.ratio = self.size[0]/self.size[1]
        self.default_size = [1280,720]
        self.scale = self.size[0]/self.default_size[0]
        with self.canvas:
            Color(0, 0, 1, 1)
            print(self.ratio)
            Rectangle(pos=self.pos, size=[100*self.scale,100*self.scale])
            Color(1, 0, 0, 0.5)
            Rectangle(pos=[25,25], size=[100*self.scale,100*self.scale])
        
        return

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    
    MyApp().run()
    
    pass
