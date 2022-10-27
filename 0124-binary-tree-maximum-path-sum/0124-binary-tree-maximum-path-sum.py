# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = root.val
        
        def maxPath(root):
            
            if root == None:
                return 0
            
            node = root.val
            left = max(0, maxPath(root.left))
            right = max(0, maxPath(root.right))
            
            self.res = max(self.res, node + left + right)
            
            return max(node + left, node + right)
        
        maxPath(root)
        
        return self.res