# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # O(n)
        
        def dfs(root):
            
            if root == None:
                return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            withR = root.val + left[1] + right[1]
            withoutR = max(left) + max(right)
            
            return [withR, withoutR]
        
        return max(dfs(root))