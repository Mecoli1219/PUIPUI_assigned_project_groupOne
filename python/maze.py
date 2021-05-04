from node import *
import numpy as np
import csv
import pandas
from enum import IntEnum
import math


class Action(IntEnum):
    ADVANCE = 1
    U_TURN = 2
    TURN_RIGHT = 3
    TURN_LEFT = 4
    HALT = 5
    BACK = 6


class Maze:
    
    def __init__(self, filepath):
        # TODO : read file and implement a data structure you like
		# For example, when parsing raw_data, you may create several Node objects.  
		# Then you can store these objects into self.nodes.  
		# Finally, add to nd_dictionary by {key(index): value(corresponding node)}
        self.raw_data = pandas.read_csv(filepath).values
        self.nodes = [] #adjacency list
        self.nd_dict = dict()  # key: index, value: the correspond node
        for data in self.raw_data:
            node_name = str(int(data[0]))
            nd = Node(node_name)
            for i in range(1,5):
                if not math.isnan(data[i]):
                    nd.setSuccessor(str(int(data[i])), i, int(data[i+4]))
            self.nodes.append(nd)
            self.nd_dict[node_name] = nd
        self.BFS_far_ans = []
        self.BFS_2_far_ans = []


    def getStartPoint(self):
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def getNodeDict(self):
        return self.nd_dict

    def BFS(self, nd):
        # TODO : design your data structure here for your algorithm
        # Tips : return a sequence of nodes from the node to the nearest unexplored deadend
        
        self.BFS_far(nd, [nd], 0, 0)
        route = self.BFS_far_ans
        unvisited = []
        for nd in self.nodes:
            if str(nd.index) not in route:
                unvisited.append(nd)
        while len(unvisited) > 0:
            shortest = None
            for unvisit in unvisited:
                for next_nd in unvisit.getSuccessors():
                    if next_nd[0] in route:
                        if shortest == None or shortest > next_nd[2]:
                            shortest = next_nd[2] 
            done = False
            for unvisit in unvisited:
                for next_nd in unvisit.getSuccessors():
                    if next_nd[0] in route and next_nd[2] == shortest:
                        index = route.index(next_nd[0])
                        route.insert(index, str(int(unvisit.index)))
                        route.insert(index, next_nd[0])
                        unvisited.remove(unvisit)
                        done = True
                        break
                if done:
                    break

        return route

    def BFS_far(self, pre_nd, route, longest_distance, distance):
        have_successor = False
        for next_nd in self.nd_dict[pre_nd].getSuccessors():
            if next_nd[0] not in route:
                distance += self.nd_dict[pre_nd].getDistance(next_nd[0])
                have_successor = True
                route.append(next_nd[0])
                longest_distance = self.BFS_far(next_nd[0], route, longest_distance, distance)
                route.pop()
                distance -= self.nd_dict[pre_nd].getDistance(next_nd[0])
        if not have_successor:
            if longest_distance < distance:
                longest_distance = distance
                self.BFS_far_ans = list.copy(route)
        return longest_distance

    def BFS_2(self, nd_from, nd_to):
        # TODO : similar to BFS but with fixed start point and end point
        # Tips : return a sequence of nodes of the shortest path
        
        self.BFS_2_far_ans = [nd_from]
        self.BFS_2_far(nd_from, nd_to, [nd_from], 0, 0)
        route = self.BFS_2_far_ans
        unvisited = []
        for nd in self.nodes:
            if str(nd.index) not in route:
                unvisited.append(nd)
        while len(unvisited) > 0:
            shortest = None
            for unvisit in unvisited:
                for next_nd in unvisit.getSuccessors():
                    if next_nd[0] in route:
                        if shortest == None or shortest > next_nd[2]:
                            shortest = next_nd[2] 
            done = False
            for unvisit in unvisited:
                for next_nd in unvisit.getSuccessors():
                    if next_nd[0] in route and next_nd[2] == shortest:
                        index = route.index(next_nd[0])
                        route.insert(index, str(int(unvisit.index)))
                        route.insert(index, next_nd[0])
                        unvisited.remove(unvisit)
                        done = True
                        break
                if done:
                    break
        return route

    def BFS_2_far(self, pre_nd, final, route, longest_distance, distance):
        for next_nd in self.nd_dict[pre_nd].getSuccessors():
            if next_nd[0] not in route:
                distance += self.nd_dict[pre_nd].getDistance(next_nd[0])
                route.append(next_nd[0])
                longest_distance = self.BFS_2_far(next_nd[0], final, route, longest_distance, distance)
                route.pop()
                distance -= self.nd_dict[pre_nd].getDistance(next_nd[0])
        if route[-1] == final:
            if longest_distance < distance:
                longest_distance = distance
                self.BFS_2_far_ans = list.copy(route)
        return longest_distance

    def getAction(self, car_dir, nd_from, nd_to):
        # TODO : get the car action
        # Tips : return an action and the next direction of the car if the nd_to is the Successor of nd_to
		# If not, print error message and return 0
        direction = self.nd_dict[nd_from].getDirection(nd_to)
        if Direction(int(car_dir)) == direction:
            return Action(1)
        if car_dir == "1":
            if direction == Direction(2):
                return Action(2)
            if direction == Direction(3):
                return Action(4)
            if direction == Direction(4):
                return Action(3)    
        if car_dir == "2":
            if direction == Direction(1):
                return Action(2)
            if direction == Direction(3):
                return Action(3)
            if direction == Direction(4):
                return Action(4)
        if car_dir == "3":
            if direction == Direction(4):
                return Action(2)
            if direction == Direction(1):
                return Action(3)
            if direction == Direction(2):
                return Action(4)
        if car_dir == "4":
            if direction == Direction(3):
                return Action(2)
            if direction == Direction(1):
                return Action(4)
            if direction == Direction(2):
                return Action(3)

        print("Error: getAction not found!")
        return 0

    def strategy(self, nd):
        return self.BFS(nd)

    def strategy_2(self, nd_from, nd_to):
        return self.BFS_2(nd_from, nd_to)
