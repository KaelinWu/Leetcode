# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
     
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        max_dia = [0]
        def depth(root, max_dia):
            if not root:
                return 0
            left = depth(root.left, max_dia)
            right = depth(root.right, max_dia)
            max_dia[0] = max(max_dia[0], left + right)

            return max(left, right) +1
        
        depth(root, max_dia)
        return max_dia[0]
            