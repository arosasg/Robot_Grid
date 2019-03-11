class Heuristics:
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

