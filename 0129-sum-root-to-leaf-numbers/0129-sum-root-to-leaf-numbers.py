# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        return self.traverse(root, 0)
        
        
    def traverse(self, root, x):
        
        if root == None:
            return 0
        
        x = (x*10 + root.val)
        
        if root.left == None and root.right == None:
            return x
        
        return self.traverse(root.left, x) + self.traverse(root.right, x)