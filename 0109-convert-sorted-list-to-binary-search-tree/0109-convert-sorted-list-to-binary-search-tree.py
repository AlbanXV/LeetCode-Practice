# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        res = []
        
        root = head
        
        while root:
            res.append(root.val)
            
            root = root.next
        
        return self.sortArr(res)
        
        
    
    def sortArr(self, head):
        n = len(head)
        
        if n == 0:
            return None
        
        if n == 1:
            return TreeNode(head[0])
        
        root = TreeNode(head[n//2])
        
        root.left = self.sortArr(head[:n//2])
        root.right = self.sortArr(head[n//2+1:])
        
        return root
        
        