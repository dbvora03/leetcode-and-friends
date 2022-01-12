# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            root = TreeNode(val)
            return root
        
        
        def recursion(root):
            
            if root is None:
                return 
        
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return
                else:
                    return recursion(root.left)
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                    return
                else:
                    return recursion(root.right)
        
        recursion(root)
        return root