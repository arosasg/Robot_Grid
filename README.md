# Robot_Grid
Two robots moving in a grid to search their goal state.

# Main Objective
The purpose of this assignment is to implement the search algorithms: breadth first search (BFS),depth first search (DFS), iterative deepening search (IDE), and A* search. 

# The setting: 
we will use the 2 robots moving in a grid as the problem that needs to be solved. The robots cannot swap positions, or hit each other. Also, they need to remain on the grid.

# Future Updates:
- Plot all the search times, states explored and frontier for different sizes and for different search algorithms.
- Fix all the random problem objects to be created to have a more accurate report of the search methods.
- Draw the robots exploration path in the grid.

# How to use the program?
Run robot.py in terminal, followed by 9 parameteres, in this order: 
1. size 
2. initial state for robot 1 x coordinate
3. initial state for robot 1 y coordinate
4. initial state for robot 2 x coordinate
5. initial state for robot 2 y coordinate
6. goal state for robot 1 x coordinate
7. goal state for robot 1 y coordinate
8. goal state for robot 2 x coordinate
9. goal state for robot 2 y coordinate

So for example in the terminal we run: .../robot.py 13 2 1 7 9 3 4 5 8

That would give us a grid of size 13x13, initial state of ((2,1),(7,9)) and goal state of ((3,4),(5,8)).

Please make sure to introduce the initial state and goal states tuple values on the range of the grid, so if the size is 13,
our initial state and goal state coordinates should range from 0 to 12 (basically from 0 to n-1). 

Notice that 4 more random problems were created to have a stronger confidence comparing search algorithms.
