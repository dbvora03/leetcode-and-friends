# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        all_nodes = []
        min = 100000
        def recursion(node):
            if node is None:
                return
            
            recursion(node.left)
            all_nodes.append(node.val)
            recursion(node.right)
        
        recursion(root)
        
        for i in range(len(all_nodes) - 1):
            if all_nodes[i + 1] - all_nodes[i] < min:
                min = all_nodes[i + 1] - all_nodes[i]
        
        return min
        