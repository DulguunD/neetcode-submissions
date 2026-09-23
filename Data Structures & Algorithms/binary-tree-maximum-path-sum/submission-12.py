# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # maximum sum so far, that's encountered continiously
        maxSum = root.val

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            
            maxLeft = max(0, dfs(node.left))
            maxRight = max(0, dfs(node.right))
            maxSum = max(maxSum, node.val+maxLeft+maxRight)

            # get the better path
            return max(maxLeft, maxRight)+node.val
        
        dfs(root)
        return maxSum