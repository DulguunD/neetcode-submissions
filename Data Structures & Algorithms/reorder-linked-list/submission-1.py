# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        node = head
        cur = head
     
        while cur:
            nextNode = cur.next
            stack.append(cur)
            cur = cur.next

        while stack:
            cache = node.next
            last = stack.pop()
            if last is node:
                last.next = None
                return
       
            if cache is node:
                cache.next = None
                return
            node.next = last
            last.next = cache
            node = cache