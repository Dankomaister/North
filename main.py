
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.core.window import Window

from game_map import World
from game_player import Player
from game_enemies import Enemy1

Config.set('input', 'mouse', 'mouse,disable_multitouch')

class Game(Widget):
    
    def __init__(self):
        super(Game, self).__init__()
        
        self.map = World(map_file='graphics/map.png')
        
        self.player = Player(id='player1',position=[100, 100])
        self.enemy1 = Enemy1(id='enemy1',position=[400, 400])
        self.enemy2 = Enemy1(id='enemy2',position=[500, 800])
        self.enemy3 = Enemy1(id='enemy3',position=[600, 400])
        self.enemy4 = Enemy1(id='enemy4',position=[700, 800])
        self.enemy5 = Enemy1(id='enemy5',position=[800, 400])
        self.enemy6 = Enemy1(id='enemy6',position=[900, 800])
        self.enemy7 = Enemy1(id='enemy7',position=[1000, 400])
        self.enemy8 = Enemy1(id='enemy8',position=[1100, 800])
        
        self.add_widget(self.map)
        self.map.add_widget(self.player)
        self.map.add_widget(self.enemy1)
        self.map.add_widget(self.enemy2)
        self.map.add_widget(self.enemy3)
        self.map.add_widget(self.enemy4)
        self.map.add_widget(self.enemy5)
        self.map.add_widget(self.enemy6)
        self.map.add_widget(self.enemy7)
        self.map.add_widget(self.enemy8)
        
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
        return
    
    def update(self, dt):
        self.map.update()
        
        return

class GameApp(App):
    def build(self):
        game = Game()
        Window.size = [800, 800]
        return game

if __name__ == "__main__":
        
        GameApp().run()
        
        
