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
        stack_values = []
     
        while cur:
            nextNode = cur.next
            stack.append(cur)
            stack_values.append(cur.val)
            cur = cur.next

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

        while stack:
            # print(f"\t\tcurrent node value: {node.val}")
            # printList(head)
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