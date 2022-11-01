# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # O(n)
        
        if root == None:
            return None
        
        queue = [root]
        res = []
        
        while queue:
            
            n = len(queue)
            
            for i in range(n):
                q = queue.pop(0)
                       
                if q.left:
                    queue.append(q.left)
                    
                if q.right:
                    queue.append(q.right)
                    
                if i == n - 1:
                    res.append(q.val)
                    
                    
        
        return res
        