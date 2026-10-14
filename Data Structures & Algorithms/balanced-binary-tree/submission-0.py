# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        # get max depth of left and right subtree and return max height

        def dfs(node):
            if not node:
                return 0
            nonlocal balanced
            
            if balanced == False:
                return 0

            
            left = dfs(node.left)
            right = dfs(node.right)

            diff = abs(left - right)
            if diff > 1:
                balanced = False

            return max(left, right) + 1


        dfs(root)

        return balanced
        