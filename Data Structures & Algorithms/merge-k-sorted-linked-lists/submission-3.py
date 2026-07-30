# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lastHead = None
        def mergeTwoLists(list1, list2):
            l1, l2 = list1, list2
            merged = ListNode()
            tail = merged
            while l1 and l2:
                if l1.val <= l2.val:
                    # take l1 value
                    tail.next = l1
                    l1 = l1.next
                else:
                    # take l2 value
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            tail.next = l1 if l1 else l2
            return merged.next

        length = len(lists)
        for i in range(1, length):
            lists[i] = mergeTwoLists(lists[i-1], lists[i])
            if i == length-1:
                lastHead = lists[i]

        return lastHead
        