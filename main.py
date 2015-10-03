
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
        
        self.player = Player([400, 400])
        self.enemy1 = Enemy1([400, 400])
        
        self.add_widget(self.map)
        self.map.add_widget(self.player)
#         self.map.add_widget(self.enemy1)
        
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
        return
    
    def update(self, dt):
        self.map.update()
#         self.player.update(self.map)
#         self.enemy1.update(self.map)
        
        return

class GameApp(App):
    def build(self):
        game = Game()
        Window.size = [800, 800]
        return game

if __name__ == "__main__":
        
        GameApp().run()
        
        
