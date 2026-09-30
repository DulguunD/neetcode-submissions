# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        left = root.left
        right = root.right

        cache = left
        root.left = right
        root.right = cache
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        