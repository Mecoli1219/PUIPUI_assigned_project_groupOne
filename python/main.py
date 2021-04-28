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
    maze = mz.Maze("data/small_maze.csv")
    point = score.Scoreboard("data/UID.csv", "team_NTUEE")
    interf = interface.interface()
    # TODO : Initializ1e necessary variables

    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting")
        mode = input("Enter which BFS you want:(BFS, BFS_2)")
        direction = 2 #input("Enter the initial direction:(1,2,3,4)")
        if mode == "BFS":
            init = input("Enter the start node:")
            route = maze.strategy(init)
        if mode == "BFS_2":
            init = input("Enter the start node:")
            end = input("Enter the final node:")
            route = maze.strategy_2(init, end)
        start = 0

        while(start < (len(route)-1)):
            command = interf.get_command()
            print(command)
            if command == "n":
                action = maze.getAction(direction, route[start], route[start + 1])
                interf.send_action(action)
                direction = str(int(maze.nd_dict[route[start]].getDirection(route[start + 1])))
                start += 1
        interf.send_action(mz.Action(5))        

        print(route)
        # TODO : for treasure-hunting, which encourages you to hunt as many scores as possible
        
    elif (sys.argv[1] == '1'):
        print("Mode 1: Self-testing mode.")
        # TODO: You can write your code to test specific function.

    interf.end_process()

if __name__ == '__main__':
    main()
