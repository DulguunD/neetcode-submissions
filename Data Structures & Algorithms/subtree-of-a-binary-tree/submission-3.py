# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if root is None and subRoot is None:
                return True
            
            if root is None or subRoot is None:
                return False

            if root.val != subRoot.val:
                return False
        
            return check(root.left, subRoot.left) and check(root.right, subRoot.right)
        
        def dfs(node) -> bool:
            if not node:
                return False

            if check(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        