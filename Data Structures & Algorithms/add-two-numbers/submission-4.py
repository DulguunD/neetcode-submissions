# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        remainder = 0
        while l1 and l2:
            total = l1.val+l2.val+remainder
            remainder = 0
            value = total
            if value >= 10:
                value = int(str(total)[1])
                remainder = int(str(total)[0])   

            node.next = ListNode(value, node.next)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val+remainder
            remainder = 0
            value = total
            if value >= 10:
                value = int(str(total)[1])
                remainder = int(str(total)[0])   
                     
            node.next = ListNode(value, node.next)
            node = node.next
            l1 = l1.next
            
        while l2:
            total = l2.val + remainder
            remainder = 0
            value = total
            if value >= 10:
                value = int(str(total)[1])
                remainder = int(str(total)[0])   
                     
            node.next = ListNode(value, node.next)
            node = node.next
            l2 = l2.next

        if remainder > 0:
            node.next = ListNode(remainder, node.next)
            node = node.next

        return dummy.next
        