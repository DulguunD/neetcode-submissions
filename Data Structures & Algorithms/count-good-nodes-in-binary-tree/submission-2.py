# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result = []
        self.count = 0

        def traverse(node: ListNode, maxNum: int):
            if not node:
                return
            # node = node.right
            # print(f"nodes: {result}")
            if node.val >= maxNum and node.val >= root.val:
                self.count+=1
                maxNum = max(maxNum, node.val)
                result.append(node.val)

            traverse(node.right, maxNum)
            traverse(node.left, maxNum)

        traverse(root, -101)
        # return len(result)
        return self.count
        