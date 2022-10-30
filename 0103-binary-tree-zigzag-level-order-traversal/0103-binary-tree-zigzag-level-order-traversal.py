# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = [root]
        res = []
        
        normal = True
        
        while queue:
            level = []
            
            for i in range(len(queue)):
                node = queue.pop(0) # or popleft()
                
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                res.append(level)
            
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        
        return res