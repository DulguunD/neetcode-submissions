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
        # current = head
        # indexes = {}
        length = 0

        # while current:
        #     positions[current.val] = current

        while old:
            # print(f"\t * * * old value: {old.val}")
            positions[index] = old
            randoms[index] = old.random
            # indexes[index] = old.val
            # print(f"index: {index}, position: {old}, random: {old.random}")
            newNode = Node(old.val, node.next, None)        
            index += 1          
            node.next = newNode
            node = node.next
            old = old.next

        length = index
        # print(f"POSITIONS: {positions}")
        # print("*    *   *   *")
        # print(f"RANDOMS: {randoms}")

            
        cur = dummy.next
        current = dummy.next
        new_positions = {}
     
        for i in range(length):
            # print(f"assigning: {i}, value: {indexes[i]},  new location: {current}")
            new_positions[i] = current
            current = current.next

        value_to_key = {v: k for k, v in positions.items()}
        for ind in range(length):
            if randoms[ind]:
                pos = value_to_key[randoms[ind]]
                # print(f"pos: {pos}")
                cur.random = new_positions[pos]
            cur = cur.next
        
        return dummy.next

        