# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(left, right):
            
            res = []
            
            if left > right:
                return [None]
            
            for i in range(left, right + 1):
                lft = helper(left, i-1)
                rght = helper(i+1, right)
                
                for l in lft:
                    for r in rght:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            return res
        
        return helper(1, n)