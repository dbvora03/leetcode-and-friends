# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = {}
        
        if not root:
            return None
                    
        def dfs(node, depth):
            
            if not node:
                return 
            
            if depth not in values:
                values[depth] = [node.val]
            else:
                values[depth].append(node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        return values.values()