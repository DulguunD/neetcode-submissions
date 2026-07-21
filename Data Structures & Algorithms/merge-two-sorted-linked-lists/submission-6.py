# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = list1
        l1, l2 = list1, list2
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            # print(f"l1: {l1.val}, l2: {l2.val}")
            if l1.val <= l2.val:
                # take l1 value
                print(f"take LIST 1---- {l1.val} to the list")
                nextNode = l1.next
                tail.next = l1
                tail = l1
                l1 = nextNode
            else:
                # take l2 value
                nextNode = l2.next
                print(f"take LIST 2---- {l2.val} to the list")
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
            tail = tail.next
            l2 = nextNode
     
        return dummy.next

        