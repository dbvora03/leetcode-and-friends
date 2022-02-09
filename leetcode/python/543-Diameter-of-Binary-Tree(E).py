# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        
        def recursion(node):
                    
            if not node:
                return 0
        
            left_side = recursion(node.left)
            right_side = recursion(node.right)
            
            self.diameter = max(self.diameter, left_side + right_side)
            
            return 1 + max(left_side, right_side)
    
        recursion(root)
        
        return self.diameter
