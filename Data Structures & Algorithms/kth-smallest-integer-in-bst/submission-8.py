# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
      def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def dfs(node: TreeNode, k):
            if not node:
                return -1

            #left side
            result = dfs(node.left, k)
            if result != -1:
                return result

            self.count += 1
            if self.count == k:
                return node.val

            #right side 
            result = dfs(node.right, k)
            if result != -1:
                return result
            return -1

        return dfs(root, k)