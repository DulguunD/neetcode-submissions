# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        lvls = []
        node = root

        def traverse(node, level):
            print(f"result: {result}")
            if level not in lvls:
                if node:
                    lvls.append(level)
                    result.append(node.val)

            if node:
                print(f"node value: {node.val}")
                # result.append(node.val)
                traverse(node.right, level+1)
                traverse(node.left, level+1)
            
        traverse(root, 0)
        return result
        