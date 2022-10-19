# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.tot = 0
        
        def tilt(root):
            
            if root == None:
                return 0
            
            left = tilt(root.left)
            right = tilt(root.right)
            
            self.tot += abs(left - right)
            
            return root.val + left + right
        
        tilt(root)
        
        return self.tot
            
            
        