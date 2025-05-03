# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root):
            if not root:
                return 0
            
            left = 1 + depth(root.left)
            right = 1 + depth(root.right)
            if right == 0 or left == 0:
                return -1
            elif abs(left - right) > 1:
                return -1
            return max(left,right)

        if depth(root) == -1:
            return False
        return True
        