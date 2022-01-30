# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def recursion(node, path):
            
            if not node:
                path.sort()
                self.ans = max(path[-1] - path[0], self.ans)
                return
        
            path_copy = path.copy()
            path_copy.append(node.val)
            
            recursion(node.left, path_copy)
            recursion(node.right, path_copy)
        
        recursion(root, [])
        
        return self.ans
            