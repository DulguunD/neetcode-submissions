# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        h = head
        prev = None
        current = head
        while current:
            print(f"current: {current.val}")
            nxt = current.next # next
            current.next = prev
            prev = current
            current = nxt

            # nxt = current.next
            # # 
            # processing = current

            # nxt.next = current
            # # prev = current.next
            # current = nxt.next
        
        # print(f"list: {})/'
        return prev

        # while 
        