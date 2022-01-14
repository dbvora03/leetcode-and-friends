# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        self.min_depth = float("+Inf")
        
        if root is None:
            return 0
        
        def dfs(node, depth):
            
            if node.right is None and node.left is None:
                self.min_depth = min(self.min_depth, depth)
            
            if node.right:
                dfs(node.right, depth + 1)
            
            if node.left:
                dfs(node.left, depth + 1)
                
            
        dfs(root, 1)
        return self.min_depth
        