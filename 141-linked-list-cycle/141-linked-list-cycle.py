# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
            
        
        
        