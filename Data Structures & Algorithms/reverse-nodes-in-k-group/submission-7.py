# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        def traverse(n, node):
            while node and n > 1:
                n -= 1
                node = node.next
            return node

        current = head
        prev = None
        while current:
            node = current
            starts = node
            ends = traverse(k, node)
            if not ends:
                return dummy.next
            next_group = ends.next # cache
           
            prev = group_prev
            while node != next_group:
                nxt = node.next # next
                node.next = prev
                prev = node
                node = nxt
            group_prev.next = ends 
            current.next = next_group 
            group_prev = current # tail
            
            # current = current.next
            current = next_group
        return dummy.next