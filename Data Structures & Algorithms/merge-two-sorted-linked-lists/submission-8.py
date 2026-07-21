# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        merged = ListNode()
        tail = merged
        while l1 and l2:
            if l1.val <= l2.val:
                # take l1 value
                nextNode = l1.next
                tail.next = l1
                tail = l1
                l1 = nextNode
            else:
                # take l2 value
                nextNode = l2.next
                tail.next = l2
                tail = l2
                l2 = nextNode

        while l1:
            nextNode = l1.next
            tail.next = l1
            tail = l1
            l1 = nextNode        

        while l2:
            nextNode = l2.next
            tail.next = l2
            tail = l2
            l2 = nextNode
     
        return merged.next

        