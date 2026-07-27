# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def printList(head: Optional[ListNode]):
            print("*    *   *   *   *")
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
        current = head
        n = k
        dummy = ListNode()
        group_prev = dummy

        if k==1:
            return head

        def traverse(n, node):
            group_starts = node
            while node and n > 1:
                n -= 1
                node = node.next
            return [group_starts, node]

        index = 0
        prev = None
        while current:
            # print(f"current: {current.val}")

            # printList(current)
            if index%k==0:
                node = current
                starts, ends = traverse(k, node)
                if not ends:
                    return dummy.next
                # print(f"starts: {starts.val}, ends: {ends.val}")
                # prev = dummy
                prev = group_prev
                # print(f"group_prev: {group_prev.val}")
                # if prev:
                #     print(f"prev: {prev.val}")
                # prev = group_prev
                comes_after = ends.next
                while node != comes_after:
                    nxt = node.next # next
                    node.next = prev
                    prev = node
                    node = nxt
                # printList(prev)
                # printList(group_prev)
                # printList(node)


                # print(f"Finished reversing prev: {prev.val}, current: {current.val}, current.next: {current.next.val}, comes_after: {comes_after.val}")
                # print(f"Finished reversing current: {current.val}, comes_after: {comes_after.val}")
                # print(f"Finished reversing current next: {current.next.val}, comes_after: {comes_after.val}")

                # group_prev = current
                group_prev.next = prev
                current.next = comes_after # nextGroup
                group_prev = current
                # group_prev = current


            index += k
            # group
            # print(f"current: {current.val}, prev.val: {prev.val}")
            # if current.next:
            #     print(f"current: {current.val}, current next: {current.next.val}")

            current = current.next

        # return prev
        return dummy.next