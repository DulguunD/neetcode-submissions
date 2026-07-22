# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head.next
        cur = head
        half = 0

        while fast and fast.next:
            half += 1
            cur = cur.next
            fast= fast.next.next

        if fast: 
            length = (half+1)*2
        else: 
            length = half*2+1

        pos_to_update = length-n-1

        # remove first element
        if pos_to_update < 0:
            return head.next

        i = 0
        node = head
        while i < pos_to_update:
            i += 1
            node = node.next

        cache = node.next.next
        node.next = cache
        return head



