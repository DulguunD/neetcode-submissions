# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        result = ListNode()
        res = None
        while current1 and current2:
            # print(f"current1: {current1.val}, current2: {current2.val}, result: {result.val}")
            if current1.val <= current2.val:
                newNode = ListNode(current1.val, current1.next)
                result.next = newNode
                result = newNode
                # print(f"\tcurrent1.next val: {current1.val}")
                current1 = current1.next
            else:
                newNode = ListNode(current2.val, current2.next)
                result.next = newNode
                result = newNode
                # print(f"current2.next val: {current2.next.val}")
                current2 = current2.next
            if not res:
                res = result

        while current1:
            newNode = ListNode(current1.val, current1.next)
            result.next = newNode
            result = newNode
            current1 = current1.next
            if not res:
                res = result

        while current2:
            newNode = ListNode(current2.val, current2.next)
            result.next = newNode
            result = newNode
            current2 = current2.next
            if not res:
                res = result
        # print(f"result: {result.val}, current1: {current1}, {current2}")
        # return result
        return res

        