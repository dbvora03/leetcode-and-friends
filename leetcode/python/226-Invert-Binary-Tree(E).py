# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        
        if root is None:
            return None
        
        left_side = self.invertTree(root.right)
        right_side = self.invertTree(root.left)
        
        root.left = left_side
        root.right = right_side
        
        return root