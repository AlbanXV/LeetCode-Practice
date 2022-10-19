# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if root == None:
            return 0
        
        self.tot = 0
        
        self.dfs(root, low, high)
        
        return self.tot
        
        
    
    def dfs(self, root, low, high):
        
        if root:
            if low <= root.val <= high:
                self.tot += root.val
            
            if low < root.val:
                self.dfs(root.left, low, high)
                
            if high > root.val:
                self.dfs(root.right, low, high)
        