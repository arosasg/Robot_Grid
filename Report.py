from collections import defaultdict, Counter
import Node

class CountCalls:
    """Delegate all attribute accesses to the object, and count them in ._counts"""
    def __init__(self, obj):
        self._object = obj
        self._counts = Counter()
        
    def __getattr__(self, attr):
        self._counts[attr] += 1
        return getattr(self._object, attr)
        
def report(searchers, problems):
    "Show metrics for each searcher on each problem."
    for searcher in searchers:
        print(searcher.__name__ + ':')
        total_counts = Counter()
        for p in problems:
            prob   = CountCalls(p)
            soln   = searcher(prob)
            counts = prob._counts; 
            counts.update(len=len(Node.path_actions(soln[0])), cost=soln[0].path_cost, frontier=soln[1])
            total_counts += counts
            report_line(counts, type(p).__name__, p)
        report_line_total(total_counts, 'TOTAL\n')
        
def report_line(counts, name, p):
    "Print one line of the report."
    print('initial {} | goal {} |{:9,d} explored |{:7,d} goal |{:5.0f} cost |{:3d} steps |{:5d} frontier| {}'
          .format(p.initial, p.goal, counts['result'], counts['is_goal'], 
                  counts['cost'], counts['len'], counts['frontier'], name))

def report_line_total(counts, name):
    "Print one line of the report."
    print('{:59,d} explored |{:7,d} goal |{:5.0f} cost |{:3d} steps |{:5d} frontier| {}'
          .format(counts['result'], counts['is_goal'], 
                  counts['cost'], counts['len'], counts['frontier'], name))
    
def astar_heuristics(searcher, problems, heuristics):
    "Show metrics for each searcher on each problem."
    print(searcher.__name__ + ':')
    total_counts = Counter()
    for p in problems:
        for heuristic in heuristics:
            prob   = CountCalls(p)
            soln   = searcher(prob, heuristic)
            counts = prob._counts; 
            counts.update(len=len(Node.path_actions(soln[0])), cost=soln[0].path_cost, frontier=soln[1])
            total_counts += counts
            report_line_heuristics(counts, type(p).__name__, heuristic, p)
    report_line_total(total_counts, 'TOTAL\n')

def report_line_heuristics(counts, name, heuristic, p):
    "Print one line of the report."
    print('initial {} | goal {} |{:9,d} explored |{:7,d} goal |{:5.0f} cost |{:3d} steps |{:5d} frontier| {}| {}'
          .format(p.initial, p.goal, counts['result'], counts['is_goal'], 
                  counts['cost'], counts['len'], counts['frontier'], name, heuristic))

