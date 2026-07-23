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
            if total >= 10:
                first = int(str(total)[1])
                second = int(str(total)[0])
                remainder = second
                print(f"first: {first}, remainder: {remainder}")
                newNode = ListNode(first, node.next)
                node.next = newNode
                node = node.next
            else:
                newNode = ListNode(total, node.next)
                node.next = newNode
                node = node.next
       
            l1 = l1.next
            l2 = l2.next
        # print(f"final remainder: {remainder}")
        while l1:
            total = l1.val + remainder
            remainder = 0
            if total >= 10:
                first = int(str(total)[1])
                second = int(str(total)[0])
                remainder = second
                # print(f"first: {first}, remainder: {remainder}")
                newNode = ListNode(first, node.next)
                node.next = newNode
                node = node.next
            else:
                newNode = ListNode(total, node.next)
                node.next = newNode
                node = node.next
            l1 = l1.next
        while l2:
            total = l2.val + remainder
            remainder = 0
            if total >= 10:
                first = int(str(total)[1])
                second = int(str(total)[0])
                remainder = second
                # print(f"first: {first}, remainder: {remainder}")
                newNode = ListNode(first, node.next)
                node.next = newNode
                node = node.next
            else:
                newNode = ListNode(total, node.next)
                node.next = newNode
                node = node.next
            l2 = l2.next
        if remainder > 0:
            newNode = ListNode(remainder, node.next)
            node.next = newNode
            node = node.next
        # if remainder >= 0:
        #     print(f"there is remainder left: {remainder}")
            #
        return dummy.next
        