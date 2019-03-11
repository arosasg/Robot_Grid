class Problem(object):
    """The abstract class for a formal problem. You should subclass this,
    overriding `actions` and `results`, and other methods if desired.
    The default heuristic is 0 and the default step cost is 1 for all states.
    Subclasses can use other keywords besides initial and goal."""

    robot_actions = [(1,0),(0,1),(-1,0),(0,-1)]
    
    def __init__(self, initial=None, goal=None, x=None, **kwds): 
        self.__dict__.update(initial=initial, goal=goal,x=None, **kwds) 
        
    def actions(self, state): raise NotImplementedError
            
    def result(self, state, action): raise NotImplementedError
    
    def is_goal(self, state):
        return state == self.goal
    
    def is_goal1(self, state):
        return state[0] == self.goal[0]
    
    def is_goal2(self, state):
        return state[1] == self.goal[1]
    
    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1
    
    def h(self, node): raise NotImplementedError                    

