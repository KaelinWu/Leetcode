"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if not root.children:
            return 1
        res = 0
        for child in root.children:
            res = max(res,self.maxDepth(child)+1)
        return res

        