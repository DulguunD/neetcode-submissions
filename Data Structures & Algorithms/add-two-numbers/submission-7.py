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
        while l1 or l2 or remainder:
            total = remainder
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            remainder = 0
            value = total
            if value >= 10:
                value = int(str(total)[1])
                remainder = int(str(total)[0])   

            node.next = ListNode(value, node.next)
            node = node.next

        return dummy.next
        