# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head.next

        cur = head
        half = 0
        while fast and fast.next:
            print(f"cur val: {cur.val}, fast val: {fast.val}")
            half += 1
            cur = cur.next
            fast= fast.next.next
        print(f"LENGTH before update: {half}")

        if fast: 
            print(f"* * final cur val: {cur.val}, fast val: {fast.val}")
            print(f"fast: {fast.val}")
            length = (half+1)*2
        else: 
            print(" FAST is None")
            length = half*2+1

        print(f"LENGTH after update: {length}")
        pos_to_remove = length - n
        pos_to_update = pos_to_remove-1
        print(f"pos_to_update: {pos_to_update}")

        if pos_to_update < 0:
            return head.next

        if pos_to_update < half:
            i = 0
            node = head
        else:
            i = half
            node = cur
            print(f"cur val: {cur.val}")
        print(f"i: {i}")

        # i = 0
        # node = head

        while i < pos_to_update:
            i += 1
            node = node.next
         
        cache = node.next.next
        node.next = cache
        return head




