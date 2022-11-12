"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root == None:
            return None
        
        queue = deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            right = None
            
            for _ in range(n):
                current = queue.popleft()
                current.next = right
                right = current
                
                if current.right:
                    queue.append(current.right)
                    queue.append(current.left)
                    # queue.extend([current.right, current.left])
        
        return root