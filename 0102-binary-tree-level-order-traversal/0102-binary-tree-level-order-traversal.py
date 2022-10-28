# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return None
        
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            cur = []
            
            for i in range(len(queue)):
                u = queue.popleft()
                cur.append(u.val)
                
                if u.left:
                    queue.append(u.left)
                if u.right:
                    queue.append(u.right)
            
            res.append(cur)
        return res