#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Question 1 :Depth-first search.
graph = {}
graph["S"] = ["A", "B"]
graph["A"] = ["C", "B", "D"]
graph["C"] = ["E", "D"]
graph["D"] = ["E", "G"]
graph["B"] = ["D"]
graph["E"] = ["G"]
graph["D"] = ["G"]

from collections import deque
def dfs(nodeName):
    if nodeName != '':
        start = 'S'
        goal = 'G'
        fringe = deque()
        fringe += graph[nodeName]
        #用于记录检查过的node
        expended = []
        #用于记录路径
        path = [goal] 
        parents = dict()
        parents['A'] = 'S'
        parents['B'] = 'S'
    else:
        print(nodeName + ' is null ! ')
        return -1
    while fringe:
        print(fringe)
        node = fringe.pop()
        if node not in expended:
            if node == goal:
                key = goal
                while key != start:
                    father = parents[key]
                    path.append(father)
                    key = father
                path.reverse()
                break
            else:
                fringe += graph[node]
                for value in graph[node]:
                    if value not in parents:
                        parents[value] = node
                expended.append(node)
    return path

print(dfs('S'))


# In[26]:


# Question 1 :Breadth-first search
graph = {}
graph["S"] = ["A", "B"]
graph["A"] = ["C", "B", "D"]
graph["C"] = ["E", "D"]
graph["D"] = ["E", "G"]
graph["B"] = ["D"]
graph["E"] = ["G"]
graph["D"] = ["G"]

from collections import deque
def bfs(nodeName):
    if nodeName != '':
        start = 'S'
        goal = 'G'
        fringe = deque()
        fringe += graph[nodeName]
        #用于记录检查过的node
        expended = []
        #用于记录路径
        path = [goal] 
        parents = dict()
        parents['A'] = 'S'
        parents['B'] = 'S'
    else:
        print(nodeName + ' is null ! ')
        return -1
    while fringe:
        print(fringe)
        node = fringe.popleft()
        if node not in expended:
            if node == goal:
                key = goal
                while key != start:
                    father = parents[key]
                    path.append(father)
                    key = father
                path.reverse()
                break
            else:
                fringe += graph[node]
                for value in graph[node]:
                    if value not in parents:
                        parents[value] = node
                expended.append(node)
    return path

print(bfs('S'))


# In[34]:


# Question 1 :Uniform cost search
graph = {}
#graph["S"] = ["A", "B"]
graph["S"] = {}
graph["S"]["A"] = 1
graph["S"]["B"] = 1
#graph["A"] = ["C", "B", "D"]
graph["A"] = {}
graph["A"]["C"] = 2
graph["A"]["B"] = 1
graph["A"]["D"] = 3
#graph["C"] = ["E", "D"]
graph["C"] = {}
graph["C"]["E"] = 3
graph["C"]["D"] = 1
#graph["D"] = ["E", "G"]
graph["D"] = {}
graph["D"]["E"] = 1
graph["D"]["G"] = 4
#graph["B"] = ["D"]
graph["B"] = {}
graph["B"]["D"] = 2
#graph["E"] = ["G"]
graph["E"] = {}
graph["E"]["G"] = 1

graph["G"] = {}

# print(graph["S"].keys() )
# print(graph["S"]["A"] )

infinity = float("inf")
costs = {}
costs["A"] = 1
costs["B"] = 1
costs["C"] = infinity
costs["D"] = infinity
costs["E"] = infinity
costs["G"] = infinity

parents = {}
parents["A"] = "S"
parents["B"] = "S"
parents["G"] = None
processed = []

#用于记录路径
path = ["G"]
def ucs():
    node = find_lowest_cost_node(costs)
    while node is not None: 
        cost = costs[node]  
        neighbors = graph[node]    
        for n in neighbors.keys(): 
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
                
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print('path = ',path)
    print('lowest_cost =  ',cost)
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: 
        cost = costs[node]
        if cost < lowest_cost and node not in processed: 
            lowest_cost = cost
            lowest_cost_node = node
            if lowest_cost_node == "G":
                key = "G"
                while key != "S":
                    father = parents[key]
                    path.append(father)
                    key = father
                path.reverse()
                break
    return lowest_cost_node

ucs()
