# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        '''
        if self.BalanceFactor(root) < -1:
            if self.BalanceFactor(root.right) > 0:
                return self.isBalanced(root.left)
            return False
        
        if self.BalanceFactor(root) > 1:
            if self.BalanceFactor(root.left) < 0:
                return self.isBalanced(root.right)
            return False
        return True
        '''
        
        if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        return True
    
    def Height(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return -1

        '''
        left = self.Height(root.left)
        right = self.Height(root.right)

        maxH = left

        if right > maxH:
            maxH = right
            
        return 1 + maxH
        '''

        return 1 + max(self.Height(root.left), self.Height(root.right))

    def BalanceFactor(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return self.Height(root.left) - self.Height(root.right)
    
    
        
        