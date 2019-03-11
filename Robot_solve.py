import random
import sys
import time
import numpy as np
from itertools import combinations
from Grid_problem import Grid_problem
from Heuristics import Heuristics
from Node import Node
from Queue import PriorityQueue
from Search_algorithms import BFS, DFS, IDS, astar_search
import Report

try:
    argument = sys.argv
    n = int(sys.argv[1])
    if n > 0:
        print("\nGrid was created of size {}x{}...".format(n,n))
    initial_state_1 = tuple((int(sys.argv[2]),int(sys.argv[3])))
    initial_state_2 = tuple((int(sys.argv[4]),int(sys.argv[5])))
    x1, y1 = initial_state_1
    x2, y2 = initial_state_2
    if (x1>=0 and x1< n and x2>=0 and x2< n and y1>=0 and y1< n and y2>=0 and y2< n and initial_state_1 != initial_state_2):
        print("\nCorrect coordinates for initial state of the robot")
    goal_state_1 = tuple((int(sys.argv[6]),int(sys.argv[7])))
    goal_state_2 = tuple((int(sys.argv[8]),int(sys.argv[9])))
    x1, y1 = goal_state_1
    x2, y2 = goal_state_2
    if (x1>=0 and x1< n and x2>=0 and x2< n and y1>=0 and y1< n and y2>=0 and y2< n and goal_state_1 != goal_state_2):
        print("\nCorrect coordinates for goal state of the robot")
    initial_state = (initial_state_1,initial_state_2)
    goal_state = (goal_state_1,goal_state_2)
    random_problems = int(sys.argv[10])
    if random_problems > 0:
        print("\n{} more problems were created for proper comparison of algorithms, with same grid size as input but random initial and goal states\n").format(random_problems)
except:
    print("\nThere was some errors with your inputs, please make sure to introduce them well!")

random_initial = [initial_state]
random_goal = [goal_state]
for i in range(random_problems):
    # 1. Generate Random X and Y coordinates to put goal 1 and 2
    x1,y1 = np.random.randint(n),np.random.randint(n)   
    x2,y2 = np.random.randint(n),np.random.randint(n)
    
    # 1.b Generate different goals
    while (x1 == x2 and y1 == y2) :
        x1,y1 = np.random.randint(n),np.random.randint(n)
        x2,y2 = np.random.randint(n),np.random.randint(n)
    
    state_temp = ((x1,y1),(x2,y2))
    random_goal.append(state_temp)

    # 2. We are going to start at random position for the two robots
    start_x1,start_y1 = np.random.randint(n),np.random.randint(n)
    start_x2,start_y2 = np.random.randint(n),np.random.randint(n)

    # 2.b Generate different starting locations for the robots
    while (start_x1 == start_x2 and start_y1 == start_y2) :
        start_x1,start_y1 = np.random.randint(n),np.random.randint(n)
        start_x2,start_y2 = np.random.randint(n),np.random.randint(n)
    
    state_temp = ((start_x1,start_y1),(start_x2,start_y2))
    random_initial.append(state_temp)

obstacles = []
limits = [-1,n]
for y in limits:
    for i in range (0,n):
        obstacles.append((y,i))
        obstacles.append((i,y))


p1 = Grid_problem(random_initial[0], random_goal[0], obstacles)
p2 = Grid_problem(random_initial[1], random_goal[1], obstacles)
p3 = Grid_problem(random_initial[2], random_goal[2], obstacles)
p4 = Grid_problem(random_initial[3], random_goal[3], obstacles)
p5 = Grid_problem(random_initial[4], random_goal[4], obstacles)

report1 = Report.report((BFS,DFS,IDS), (p1,p2,p3,p4,p5))
report2 = Report.astar_heuristics(astar_search, (p1,p2,p3,p4,p5), ("manhattan_distance","euclidian_distance"))

print(report1, report2)
print("\nProgram completed, all robots arrived safe to destination!!")
