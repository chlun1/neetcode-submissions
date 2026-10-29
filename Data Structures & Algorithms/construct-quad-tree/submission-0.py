"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def is_leaf(self, grid: List[List[int]]) -> bool:
        first_val = grid[0][0]
        for row in grid:
            for col in row:
                if col != first_val:
                    return False
        return True

    def get_quad(self, grid):
        mid = len(grid) // 2
        top = grid[:mid]
        bot = grid[mid:]
        top_left = [row[:mid] for row in top]
        top_right = [row[mid:] for row in top]
        bot_left = [row[:mid] for row in bot]
        bot_right = [row[mid:] for row in bot]

        return (
            top_left,
            top_right,
            bot_left,
            bot_right,
        )

    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 1 or self.is_leaf(grid):
            return Node(
                grid[0][0] == 1,
                True,
                None, None, None, None,
            )

        quad = self.get_quad(grid)

        return Node(
            0,
            False,
            self.construct(quad[0]),
            self.construct(quad[1]),
            self.construct(quad[2]),
            self.construct(quad[3]),
        )
        