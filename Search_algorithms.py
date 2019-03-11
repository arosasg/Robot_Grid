import Node
from Queue import PriorityQueue
from collections import deque
import heapq

FIFOQueue = deque

LIFOQueue = list

failure = Node.Node('failure', path_cost=float('inf')) # Indicates an algorithm couldn't find a solution.
cutoff  = Node.Node('cutoff',  path_cost=float('inf')) # Indicates iterative deeepening search was cut off.

def BFS(problem):
    "Search shallowest nodes in the search tree first."
    frontier = FIFOQueue([Node.Node(problem.initial)])
    reached = set()
    count = []
    while frontier:
        node = frontier.pop()
        count.append(node.state)
        if problem.is_goal(node.state):
            return node, len(frontier)
        for child in Node.expand(problem, node):
            s = child.state
            if s not in reached:
                reached.add(s)
                frontier.appendleft(child)
            
    return failure

def DFS(problem):
    "Search deepest nodes in the search tree first."
    frontier = LIFOQueue([Node.Node(problem.initial)])
    solution = failure
    reached = [problem.initial]
    count = []
    while frontier:
        node = frontier.pop()
        count.append(node.state)
        for child in Node.expand(problem, node):
            if problem.is_goal(child.state):
                reached.append(child.state)
                return child, len(frontier)
            s = child.state
            if s not in reached:
                reached.append(s)
                frontier.append(child)
    return solution

def depth_limited_search(problem, limit=5):
    "Search deepest nodes in the search tree first."
    frontier = LIFOQueue([Node.Node(problem.initial)])
    solution = failure
    reached = [problem.initial]
    while frontier:
        node = frontier.pop()
        if len(node) > limit:
            solution = cutoff
        else:
            for child in Node.expand(problem, node):
                if problem.is_goal(child.state):
                    reached.append(child.state)
                    return child, len(frontier)
                s = child.state
                if s not in reached:
                    reached.append(s)
                    frontier.append(child)
    return solution, None

def IDS(problem):
    "Do depth-limited search with increasing depth limits."
    for limit in range(1, 100):
        result, frontier = depth_limited_search(problem, limit)
        if result != cutoff:
            return result, frontier
        
def best_first_search(problem, f):
    "Search nodes with minimum f(node) value first."
    frontier = PriorityQueue([Node.Node(problem.initial)], key=f)
    reached = {}
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node, len(frontier)
        for child in Node.expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
    return failure, None

def astar_search(problem, heuristics=None):
    """Search nodes with minimum f(n) = g(n) + h(n)."""
    h = problem.h
    result, frontier = best_first_search(problem, f=lambda node: node.path_cost + h(node, heuristics))
    return result, frontier


class PriorityQueue:
    """A queue in which the item with minimum f(item) is always popped first."""

    def __init__(self, items=(), key=lambda x: x): 
        self.key = key
        self.items = [] # a heap of (score, item) pairs
        for item in items:
            self.add(item)
         
    def add(self, item):
        """Add item to the queuez."""
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        """Pop and return the item with min f(item) value."""
        return heapq.heappop(self.items)[1]
    
    def top(self): return self.items[0][1]

    def __len__(self): return len(self.items)

