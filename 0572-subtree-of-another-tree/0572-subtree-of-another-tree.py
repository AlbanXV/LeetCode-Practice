# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == None:
            return False
        
        if self.is_equal(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def is_equal(self, root, sub):
        if root == None and sub == None:
            return True
            
        if root and sub and root.val == sub.val:
            return self.is_equal(root.left, sub.left) and self.is_equal(root.right, sub.right)
            
        return False
            
            