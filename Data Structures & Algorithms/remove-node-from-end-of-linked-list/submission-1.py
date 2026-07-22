# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        pos_to_remove = 0

        while cur:
            length += 1
            cur = cur.next
        pos_to_remove = length - n
        # print(f"length: {length}, pos to remove: {pos_to_remove}")
       
        node = head
        i = 0
        pos_to_update = pos_to_remove-1
        print(f"pos-to_update: {pos_to_update}")
        if pos_to_update < 0:
            cache = node.next
            head = cache
            return head

        while i < pos_to_update:
            i += 1
            node = node.next


        cache = node.next.next
        # print(f"node: {node.val}, and attaching to: {node.next.val}")
        node.next = cache
        return head

        def printList(head: Optional[ListNode]):
            current = head
            visited = set()
            i = 0
            while current:
                print(f"{i}: {current.val}")
                if current in visited:
                    print("Loop detected")
                    return
                visited.add(current)
                current = current.next
                i += 1
            return
        cur = head
        start = 0
        slow = head
        header = head
        fast = head.next
        # positionToRemove = 0

        # while cur:
        #     nodeToRemove = 
        #     cur = cur.next

        # while fast and fast.next:
        #     print(f"slow: {slow.val}, fast: {fast.val}")

        #     slow = slow.next
        #     fast = fast.next.next
        #     cur = cur.next
            #
        # while fast and fast.next:
        #     n -= 1
        #     printList(slow)

        #     print(f"slow: {slow.val}, fast: {fast.val}, n: {n}")
        #     # cache = slow.next.next
        #     if n == 0:
        #         cache = slow.next.next
        #         print(f"slow.next.next: {cache.val}, setting: slow.next: {slow.next.val}")

        #         slow.next = cache
        #         slow = cache
        #         continue
        #     slow = slow.next
        #     fast = fast.next.next 
        return head