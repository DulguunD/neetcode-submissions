# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
      def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []
        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.right)
            # print(f"node: {node.val}")
            self.result.append(node.val)
            dfs(node.left)

        dfs(root)
        # print(f"FINAL RESULT: {self.result}")
        return self.result[-k]