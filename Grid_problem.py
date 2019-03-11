import math

class Grid_problem:
    """Finding a path on a 2D grid with obstacles. Obstacles are (x, y) cells."""
    
    directions = [(0,-1),(-1,0),(1, 0),(0,1)]

    def __init__(self, initial=(15, 30), goal=(130, 30), obstacles=(), **kwds):
        self.__dict__.update(initial=initial, goal=goal,obstacles=obstacles, **kwds) 
    
    def step_cost(self, s, action, s1): return 1
    
    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1
    
    def h(self, node, heuristics): 
        if (heuristics == "manhattan_distance"):
            return manhattan_distance(node.state, self.goal)
        return euclidian_distance(node.state, self.goal)
                  
    def result(self, state, action): 
        "Both states and actions are represented by (x, y) pairs."
        return action if action not in self.obstacles else state
    
    def is_valid_loc(self, state, new_state):
        if (new_state[0] == new_state[1]) or (new_state[0] == state[1] and new_state[1] == state[0]):
            return False
        return True

    def is_goal(self, state):
        return state == self.goal
    
    def is_goal1(self, state):
        return state[0] == self.goal[0]
    
    def is_goal2(self, state):
        return state[1] == self.goal[1]

    def actions(self, state):
        """You can move one cell in any of `directions` to a non-obstacle cell."""
        x, y = state[0]
        w, z = state[1]
        
        if self.is_goal1(state):
            for (dx2, dy2) in self.directions:
                if (w + dx2, z + dy2) not in self.obstacles:
                    new_state = ((x,y),(w + dx2, z + dy2))
                    if self.is_valid_loc(state, new_state):
                        yield new_state
                    
        if self.is_goal2(state):
            for (dx1, dy1) in self.directions:
                if (x + dx1, y+ dy1) not in self.obstacles:
                    new_state = ((x+dx1,y+dy1),(w,z))
                    if self.is_valid_loc(state, new_state):
                        yield new_state
        else:
            for (dx1, dy1) in self.directions:
                if (x + dx1, y + dy1) not in self.obstacles:
                    for (dx2, dy2) in self.directions:
                        if (w + dx2, z + dy2) not in self.obstacles:
                            new_state = ((x + dx1, y + dy1),(w + dx2, z + dy2))
                            if self.is_valid_loc(state, new_state):
                                yield new_state


def euclidian_distance(node, goal):
    "Straight-line distance between two 2D points."
    x1, y1 = node[0]
    w2, z2 = node[1]
    gx1, gy1 = goal[0]
    gw2, gz2 = goal[1]
    cost = math.sqrt((gx1-x1)**2 + (gy1-y1)**2 + (gw2-w2)**2 + (gz2-z2)**2)
    return cost

def manhattan_distance(node, goal):
    x1, y1 = node[0]
    w2, z2 = node[1]
    gx1, gy1 = goal[0]
    gw2, gz2 = goal[1]
    cost = abs(gx1-x1) + abs(gy1-y1) + abs(gw2-w2) + abs(gz2-z2)
    return cost

