# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        return self.traverse(root1) == self.traverse(root2)
    
    
    def traverse(self, root):
        
        if root == None:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        return self.traverse(root.left) + self.traverse(root.right)
        
        