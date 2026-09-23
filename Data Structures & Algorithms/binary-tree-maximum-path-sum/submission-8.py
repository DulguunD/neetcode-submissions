# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # maximum sum so far, that's encountered continiously
        self.maxSum = root.val

        def dfs(node, total):
            if node is None:
                return 0
            
            # print(f"\t*Path: {path}, total: {total}, node: {node.val}, max: {self.maxSum}")
            total += node.val
            self.maxSum = max(self.maxSum, total, node.val)

            # to get the sum of the subtree, starting from this node
            total = node.val
       
            left_max = dfs(node.left, total)
            right_max = dfs(node.right, total)

            result_sum = 0

            # both paths suck
            if left_max < 0 and right_max < 0:
                result_sum = total
            # right is better than left path
            elif left_max < right_max:
                result_sum = total+right_max
            # left is better than right path
            else:
                result_sum = total+left_max
            
            self.maxSum = max(self.maxSum, left_max+right_max+node.val, result_sum)
            return result_sum

        dfs(root, 0)
        return self.maxSum