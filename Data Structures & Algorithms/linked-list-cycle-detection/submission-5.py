# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            value = cur.val
            if value in seen:
                if not cur.next:
                    break
                return True
            seen.add(value)
            cur = cur.next
        return False