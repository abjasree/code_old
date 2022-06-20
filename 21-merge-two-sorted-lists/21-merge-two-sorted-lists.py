# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        elif list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
            
        
        
    def iterative_mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        sum_list = temp = ListNode(0)
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
                
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
            
        temp.next = list1 or list2
        return sum_list.next
        