'''
Created on 16 okt. 2015

@author: danhe
'''

import queue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node,all_nodes):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    for dir in dirs:
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        if neighbor in all_nodes and neighbor != (3,1):
            result.append(neighbor)
    
    return result

all_nodes = []

for x in range(6):
    for y in range(4):
        all_nodes.append((x, y))

start = (1,1)
goal = (3,3)

frontier = queue.PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()
    
    if current == goal:
        break
    
    for next in neighbors(current,all_nodes):
        if next in [(0,2),(1,2),(2,1),(3,1),(3,2),(4,1),(5,3)]:
            continue
        new_cost = cost_so_far[current] + 1
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost + heuristic(goal, next)
            frontier.put(next, priority)
            came_from[next] = current

current = goal
path = [current]
while current != start:
    current = came_from[current]
    path.append(current)
path.reverse()
print(path)


