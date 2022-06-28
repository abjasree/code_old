# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
                
        return False
    
    def brute_force_hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        node_dict = {}
        if current == None:
            return False
        while current.next != None:
            if current in node_dict.keys():
                return True
            else:
                node_dict[current] = 0
                current = current.next
                
        return False
            
        
        
        