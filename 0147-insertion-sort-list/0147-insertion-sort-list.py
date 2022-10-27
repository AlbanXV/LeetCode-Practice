# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(n^2)
        
        temp = ListNode(0)
        current = head
        
        while current:
            j = temp
            
            while j.next and j.next.val < current.val:
                j = j.next
            
            k = current.next
            current.next = j.next
            j.next = current
            current = k
            
        return temp.next