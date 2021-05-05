from node import *
import maze as mz
import score
import interface
import time

import numpy as np
import pandas
import time
import sys
import os

def main():
    maze = mz.Maze("data/medium_maze.csv")
    point = score.Scoreboard("data/UID.csv", "team_NTUEE")
    interf = interface.interface()
    # TODO : Initializ1e necessary variables

    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting")
        mode = input("Enter which BFS you want:(BFS, BFS_2)")
        direction = "1" #input("Enter the initial direction:(1,2,3,4)")
        if mode == "BFS":
            init = input("Enter the start node:")
            route = maze.strategy(init)
        if mode == "BFS_2":
            init = input("Enter the start node:")
            end = input("Enter the final node:")
            route = maze.strategy_2(init, end)
        print(route)
        start = 0
        action = maze.getAction(direction, route[start], route[start + 1])
        interf.send_action(action)
        direction = str(int(maze.nd_dict[route[start]].getDirection(route[start + 1])))
        start += 1

        while(start < (len(route)-1)):
            command = interf.get_command()
            print(command)
            if command == "n":
                action = maze.getAction(direction, route[start], route[start + 1])
                interf.send_action(action)
                if action == mz.Action(2):
                    uidcode = interf.get_UID()
                    print(uidcode)
                    point.add_UID(str(uidcode))
                    print(point.getCurrentScore())
                direction = str(int(maze.nd_dict[route[start]].getDirection(route[start + 1])))
                start += 1

#            if uidcode != 0:            
                    #point.add_UID(str(uidcode))
                    #print(point.getCurrentScore())
 #               print(uidcode)
  #              point.add_UID(str(uidcode))
   #             print(point.getCurrentScore())
            
        command = interf.get_command()
        interf.send_action(mz.Action(5))        

        print(route)
        # TODO : for treasure-hunting, which encourages you to hunt as many scores as possible
        
    elif (sys.argv[1] == '1'):
        # TODO: You can write your code to test specific function.
        print("Mode 1: for checkpoint")
        direction = "2" #input("Enter the initial direction:(1,2,3,4)")
        in_node = 1
        interf.send_action(mz.Action(1))
        while(in_node < 13):
            command = interf.get_command()
            if command == "n":
                if in_node == 1 or in_node == 2 or in_node == 3:
                    interf.send_action(mz.Action(1))
                    in_node += 1
                elif in_node == 4:
                    interf.send_action(mz.Action(3))
                    in_node += 1
                elif in_node == 5:
                    interf.send_action(mz.Action(2))
                    in_node += 1
                    uidcode = interf.get_UID()
                    print(uidcode)
                    point.add_UID(str(uidcode))
                    print(point.getCurrentScore())
                elif in_node == 6:
                    interf.send_action(mz.Action(1))
                    in_node += 1
                elif in_node == 7:
                    interf.send_action(mz.Action(3))
                    in_node += 1
                elif in_node == 8:
                    interf.send_action(mz.Action(4))
                    in_node += 1
                elif in_node == 9:
                    interf.send_action(mz.Action(3))
                    in_node += 1  
                elif in_node == 10:
                    interf.send_action(mz.Action(2))
                    in_node += 1
                    uidcode = interf.get_UID()
                    print(uidcode)
                    point.add_UID(str(uidcode))
                    print(point.getCurrentScore())
                elif in_node == 11:
                    interf.send_action(mz.Action(1))
                    in_node += 1
                elif in_node == 12:
                    interf.send_action(mz.Action(5))
                    in_node += 1      
                print(in_node)
        command = interf.get_command()
        interf.send_action(mz.Action(5))  

    elif (sys.argv[1] == '2'):
        # TODO: You can write your code to test specific function.
        print("Mode 2: for checkpoint with backward")
        direction = "2" #input("Enter the initial direction:(1,2,3,4)")
        in_node = 1
        interf.send_action(mz.Action(1))
        while(in_node < 13):
            command = interf.get_command()
            if command == "n":
                if in_node == 1 or in_node == 2 or in_node == 3:
                    interf.send_action(mz.Action(1))
                    in_node += 1
                elif in_node == 4:
                    interf.send_action(mz.Action(6))
                    in_node += 2
                    uidcode = interf.get_UID(2)
                    print(uidcode)
                    point.add_UID(str(uidcode))
                    print(point.getCurrentScore())
                elif in_node == 6:
                    interf.send_action(mz.Action(1))
                    in_node += 1
                elif in_node == 7:
                    interf.send_action(mz.Action(3))
                    in_node += 1
                elif in_node == 8:
                    interf.send_action(mz.Action(4))
                    in_node += 1
                elif in_node == 9:
                    interf.send_action(mz.Action(3))
                    in_node += 1  
                elif in_node == 10:
                    interf.send_action(mz.Action(2))
                    in_node += 1
                    uidcode = interf.get_UID()
                    print(uidcode)
                    point.add_UID(str(uidcode))
                    print(point.getCurrentScore())
                elif in_node == 11:
                    interf.send_action(mz.Action(1))
                    in_node += 1
                elif in_node == 12:
                    interf.send_action(mz.Action(5))
                    in_node += 1      
                print(in_node)

        command = interf.get_command()
        interf.send_action(mz.Action(5))  

    interf.end_process()

if __name__ == '__main__':
    main()
