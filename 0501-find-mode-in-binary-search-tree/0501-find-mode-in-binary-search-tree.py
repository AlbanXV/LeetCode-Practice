# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        cnt = {}
        
        self.traverse(root, cnt)
        
        for i, j in cnt.items():
            if j == max(cnt.values()):
                res.append(i)
        
        
        return res
        
    
    
    def traverse(self, root, x):
        
        if root == None:
            return None
        
        x[root.val] = x.get(root.val, 0) + 1
        
        self.traverse(root.left, x)
        self.traverse(root.right, x)