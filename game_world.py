'''
Created on 23 okt. 2015

@author: danhe
'''

from kivy.uix.widget import Widget
from queue import PriorityQueue
from random import randint
from game_map import Map

class GameWorld(Widget):

    def __init__(self, map_file):
        super(GameWorld, self).__init__()
        
        self.id = 'gameworld'
        
        self.map = Map(map_file)
        self.add_widget(self.map)
        
        self.build_graph()
        
        return
    
    def build_graph(self):
        
        self.nodes = []
        self.node_cost = {}
        for x in range(int(self.map.size[0] / 32)):
            for y in range(int(self.map.size[1] / 32)):
                self.nodes.append((x, y))
                self.node_cost[(x, y)] = 1
        
        self.node_cost[(1,11)] = 0
        self.node_cost[(2,11)] = 0
        self.node_cost[(3,11)] = 0
        self.node_cost[(4,11)] = 0
        self.node_cost[(5,11)] = 0
        self.node_cost[(6,11)] = 0
        self.node_cost[(7,11)] = 0
        self.node_cost[(8,11)] = 0
        self.node_cost[(1,12)] = 0
        self.node_cost[(2,12)] = 0
        self.node_cost[(3,12)] = 0
        self.node_cost[(4,12)] = 0
        self.node_cost[(5,12)] = 0
        self.node_cost[(6,12)] = 0
        self.node_cost[(7,12)] = 0
        self.node_cost[(8,12)] = 0
        self.node_cost[(1,13)] = 0
        self.node_cost[(2,13)] = 0
        self.node_cost[(3,13)] = 0
        self.node_cost[(4,13)] = 0
        self.node_cost[(5,13)] = 0
        self.node_cost[(6,13)] = 0
        self.node_cost[(7,13)] = 0
        self.node_cost[(8,13)] = 0
        self.node_cost[(2,14)] = 0
        self.node_cost[(3,14)] = 0
        self.node_cost[(4,14)] = 0
        self.node_cost[(5,14)] = 0
        self.node_cost[(6,14)] = 0
        self.node_cost[(7,14)] = 0
        self.node_cost[(8,14)] = 0
        self.node_cost[(2,15)] = 0
        self.node_cost[(3,15)] = 0
        self.node_cost[(4,15)] = 0
        self.node_cost[(5,15)] = 0
        self.node_cost[(6,15)] = 0
        self.node_cost[(7,15)] = 0
        self.node_cost[(8,15)] = 0
        
        return
    
    def neighbors(self, node):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbor_list = []
        
        for d in directions:
            neighbor = (node[0] + d[0], node[1] + d[1])
            if neighbor in self.nodes and self.node_cost[neighbor] != 0:
                neighbor_list.append(neighbor)
        
        return neighbor_list
    
    def pathfinding(self, start, goal):
        
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()
            
            if current == goal:
                break
            
            for node in self.neighbors(current):
                
                new_cost = cost_so_far[current] + self.node_cost[node]
                
                if node not in cost_so_far or new_cost < cost_so_far[node]:
                    cost_so_far[node] = new_cost
                    priority = new_cost + heuristic(goal, node)
                    frontier.put(node, priority)
                    came_from[node] = current
        
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        
        return path
    
    def update(self):
        
        for child in self.children:
            child.update()
        
        return
    
