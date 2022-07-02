# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
        
        
    def brute_force_middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp.next != None:
            length += 1
            temp = temp.next
        
        middle = length//2 if length % 2 == 0 else length//2 + 1
        count = 0
        ans = head
        while count < middle:
            count += 1
            ans = ans.next
        return ans
        
           
        
            
            
            
        