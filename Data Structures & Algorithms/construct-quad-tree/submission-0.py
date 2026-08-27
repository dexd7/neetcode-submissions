"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        flat =  [element for row in grid for element in row]
        if len(set(flat))>1:
            midPoint = len(grid)//2
            topLeft = self.construct([row[0:midPoint] for row in grid[0:midPoint]])
            topRight = self.construct([row[midPoint:len(grid)] for row in grid[0:midPoint]])
            bottomLeft = self.construct([row[0:midPoint] for row in grid[midPoint:len(grid)]])
            bottomRight = self.construct([row[midPoint:len(grid)] for row in grid[midPoint:len(grid)]])
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        return Node(grid[0][0], True)