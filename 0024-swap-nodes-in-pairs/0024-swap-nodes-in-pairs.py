# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        
        res = ListNode(None, head)
        prev = res
        current = head
        
        while current and current.next:
            prev.next = current.next
            current.next = current.next.next
            prev.next.next = current
            prev, current = current, current.next
        
        return res.next
        