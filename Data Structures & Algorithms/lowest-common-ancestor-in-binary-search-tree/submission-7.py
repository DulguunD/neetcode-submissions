# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      
        def dfs(node):
            if node is None:
                return None
            
            left = None
            right = None
            if node.val < q.val and node.val < p.val:
                right = dfs(node.right)
            elif node.val > q.val and node.val > p.val:
                left = dfs(node.left)
            else:
                return node

            # left = dfs(node.left)
            # right = dfs(node.right)

            if left and right:
                return node
            
            return left if left else right

        return dfs(root)