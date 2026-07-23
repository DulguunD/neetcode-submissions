"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        randoms = {}
        positions = {}
        index = 0
        dummy = Node(0)
        node = dummy
        old = head
        length = 0

        while old:
            positions[index] = old
            randoms[index] = old.random
            index += 1          
            node.next = Node(old.val, node.next, None)        
            node = node.next
            old = old.next

        length = index
        current = dummy.next
        new_positions = {}
        for i in range(length):
            # print(f"assigning: {i}, value: {indexes[i]},  new location: {current}")
            new_positions[i] = current
            current = current.next

        cur = dummy.next
        value_to_key = {v: k for k, v in positions.items()}
        for ind in range(length):
            if randoms[ind]:
                pos = value_to_key[randoms[ind]]
                cur.random = new_positions[pos]
            cur = cur.next
        
        return dummy.next

        