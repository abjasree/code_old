# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        previous = None
        current = head
        nex = head.next
        while current != None:
            current.next = previous
            previous = current
            current = nex
            if current != None:
                nex = current.next
        return previous
            
        
            
            