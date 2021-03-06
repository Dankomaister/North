
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.core.window import Window

from game_world import GameWorld
from game_player import Player
from game_enemies import Enemy1

Config.set('input', 'mouse', 'mouse,disable_multitouch')

class Game(Widget):
    
    def __init__(self):
        super(Game, self).__init__()
        
        self.gameworld = GameWorld(map_file='graphics/map.png')
        self.player = Player(id='player1',position=(2,2))
        
        self.add_widget(self.gameworld)
        self.gameworld.add_widget(self.player)
        
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
        return
    
    def update(self, dt):
        self.gameworld.update()
        
        return

class GameApp(App):
    def build(self):
        game = Game()
        Window.size = [800, 608]
        return game

if __name__ == "__main__":
        
        GameApp().run()
        
        
