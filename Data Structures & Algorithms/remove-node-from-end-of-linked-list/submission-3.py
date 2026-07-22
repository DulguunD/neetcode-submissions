# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        pos_to_remove = length - n
       
        node = head
        i = 0
        pos_to_update = pos_to_remove-1
        if pos_to_update < 0:
            cache = node.next
            head = cache
            return head

        while i < pos_to_update:
            i += 1
            node = node.next
            
        cache = node.next.next
        node.next = cache
        return head


