# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp.next != None:
            length += 1
            temp = temp.next
        if length % 2 == 1:  
            middle = length//2 + 1
            count = 0
            ans = head
            while count < middle:
                count += 1
                ans = ans.next
            return ans
        else:
            middle = length//2 
            count = 0
            ans = head
            while count < middle:
                count += 1
                ans = ans.next
            return ans
            
            
        