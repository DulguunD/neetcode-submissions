# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def traverse(node: TreeNode, maxNum: int):
            if not node:
                return
            if node.val >= maxNum and node.val >= root.val:
                self.count+=1
                maxNum = node.val

            traverse(node.right, maxNum)
            traverse(node.left, maxNum)

        traverse(root, root.val)
        return self.count
        