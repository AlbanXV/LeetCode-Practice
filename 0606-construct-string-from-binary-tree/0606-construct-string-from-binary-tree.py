# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        res = []
        
        if root == None:
            return ''
        
        res = str(root.val)
        
        if root.left or root.right:
            res += f"({self.tree2str(root.left)})"
        
        
        if root.right:
            res += f"({self.tree2str(root.right)})"
        
        
        return res