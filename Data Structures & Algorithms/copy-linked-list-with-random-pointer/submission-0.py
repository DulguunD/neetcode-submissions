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
        indexes = {}

        # while current:
        #     positions[current.val] = current

        while old:
            # print(f"\t * * * old value: {old.val}")
            positions[index] = old
            randoms[index] = old.random
            indexes[index] = old.val
            # print(f"index: {index}, position: {old}, random: {old.random}")
            newNode = Node(old.val, node.next, None)        
            index += 1          
            node.next = newNode
            node = node.next
            old = old.next

        # print(f"POSITIONS: {positions}")
        # print("*    *   *   *")
        # print(f"RANDOMS: {randoms}")

            
        cur = dummy.next
        current = dummy.next
        new_positions = {}
     
        for i in range(len(indexes)):
            # print(f"assigning: {i}, value: {indexes[i]},  new location: {current}")
            new_positions[i] = current
            current = current.next



        # print(f"NEW POSITIONS: {new_positions}")

        value_to_key = {v: k for k, v in positions.items()}
        
        for ind, value in indexes.items():
            # cur.random = new_positions[ke]/
            # print(f"index: {ind}, value: {value}")
            # pos = value_to_key[randoms[ind]]
            keys = [key for key, val in positions.items() if val == randoms[ind]]
            if keys:
                pos = keys[0]
                cur.random = new_positions[pos]
                # print(f"new positions: {new_positions[pos]}")
                # print(f"\tKEYS: {keys}")
            cur = cur.next
            # if randoms[ind]:
            #     keys = [key for key, val in positions.items() if val == randoms[ind]]
            #     pos = keys[0]
            #     cur.random = new_positions[pos]
            #     print(f"new positions: {new_positions[pos]}")
            #     # cur.random = keys[0]
            #     print(f"\tKEYS: {keys}")
            # else:
            #     cur.random = None

        # index = 0
        # while cur:
        #     print(f"current: {cur.val}")
        #     # cur.random = random[cur.val]
        #     # heh = positions[cur.val]
        #     # random_location = random[cur.val]
        #     if randoms[index]:
        #         keys = [key for key, val in positions.items() if val == randoms[index]]
        #         # keys = [key for key, val in randoms.items() if val == positions[index]]

        #         # cur.random = keys[0]
        #         # cur.random = positions
        #         # print(f"Index: {index}, old position: {}")
        #         cur.random = new_positions[keys[0]]
        #         print(f"\tKEYS: {keys}")

        #     else:
        #         cur.random = None
        #     # print(f"random: {randoms[cur.val]}, position: {positions[cur.val]}")
        #     cur = cur.next
        #     index += 1

        # print(f"cur: {cur}")
        return dummy.next
