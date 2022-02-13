# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        
            if root is None:
                return None
        
            cache = dict()
            
            def dfs(depth, node):
                
                if node is None:
                    return 
            
                cache[depth] = node.val
                
                dfs(depth + 1, node.left)
                dfs(depth + 1, node.right)
            
            dfs(1, root)

            return cache.values()