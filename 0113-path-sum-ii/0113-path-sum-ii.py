# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # bfs
        if root == None:
            return []
        
        res = []
        
        queue = [(root, root.val, [root.val])]
        
        while queue:
            current, val, q = queue.pop(0)
            
            if current.left == None and current.right == None and val == targetSum:
                res.append(q)
            
            if current.left:
                queue.append((current.left, val + current.left.val, q + [current.left.val]))
            
            if current.right:
                queue.append((current.right, val + current.right.val, q + [current.right.val]))
            
        
        return res