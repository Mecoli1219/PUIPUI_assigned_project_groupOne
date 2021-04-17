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

maze = mz.Maze("data/small_maze.csv")

print(maze.BFS("4"))