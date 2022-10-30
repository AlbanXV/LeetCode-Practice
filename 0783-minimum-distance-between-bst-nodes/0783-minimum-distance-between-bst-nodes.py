# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        self.res = float('inf')
        self.min = float('-inf')
        
        def inorder(root):
            if root == None:
                return None
            
            inorder(root.left)
            self.res = min(self.res, root.val - self.min)
            self.min = root.val
            inorder(root.right)
            
        inorder(root)
        
        return self.res
            