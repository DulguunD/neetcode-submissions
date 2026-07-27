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
            group_starts = node
            while node and n > 1:
                n -= 1
                node = node.next
            return [group_starts, node]

        current = head
        prev = None
        while current:
            node = current
            starts, ends = traverse(k, node)
            if not ends:
                return dummy.next
            comes_after = ends.next
            prev = group_prev
            while node != comes_after:
                nxt = node.next # next
                node.next = prev
                prev = node
                node = nxt
            group_prev.next = prev
            current.next = comes_after # nextGroup
            group_prev = current
            
            current = current.next

        return dummy.next