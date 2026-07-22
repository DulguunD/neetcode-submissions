# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head.next

        # while n>1:
        #     print(f"fast val: {fast.val}")
        #     n -= 1
        #     fast = fast.next
        # print(f"*   *   * Final fast val: {fast.val}")
        

        # while fast:
        #     fast = fast.next.next
        cur = head
        fast = head.next
        length = 0
        while fast and fast.next:
            print(f"cur val: {cur.val}, fast val: {fast.val}")
            length += 1
            cur = cur.next
            fast= fast.next.next
        print(f"LENGTH before update: {length}")

        if fast: 
            print(f"* * final cur val: {cur.val}, fast val: {fast.val}")
            print(f"fast: {fast.val}")
            length = (length+1)*2
        else: 
            print(" FAST is None")
            length = length*2+1

        print(f"LENGTH after update: {length}")
        
        # if length != 0:
        #     length = (length+1)*2

        # if length%2==0 and length != 0:
        #     length = length*2+1
        # else: 
        #     length = (length+1)*2


        print(f"LENGTH: {length}")
        pos_to_remove = length - n
        # node = head
        # i = 0
        pos_to_update = pos_to_remove-1
        print(f"pos_to_update: {pos_to_update}")

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




