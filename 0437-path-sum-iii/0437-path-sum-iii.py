# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # O(n^2)
        
        def dfs(root, summ):
            res = 0
            
            if root == None:
                return res
            
            if summ == root.val:
                res += 1
            
            res += dfs(root.left, summ-root.val)
            res += dfs(root.right, summ-root.val)
            
            return res
        
        if root is None:
            return 0
        
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        
        