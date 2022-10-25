# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.Valid(root, float(-inf), float(inf))
        
    
    def Valid(self, root, low, high):
        
        if root == None:
            return True
        
        if not (root.val < high and root.val > low):
            return False
        
        return self.Valid(root.left, low, root.val) and self.Valid(root.right, root.val, high)
    