# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: TreeNode, minNum: int, maxNum: int):
            if not node:
                return True
            if minNum is not None and node.val <= minNum:
                return False
            if maxNum is not None and node.val >= maxNum:
                return False


            # left side
            if not traverse(node.left, minNum, node.val):
                return False

            #right side
            if maxNum is not None:
                rightMax = max(maxNum, node.val)
            else:
                rightMax = maxNum
        
            if not traverse(node.right, node.val, rightMax):
                return False
            return True

        return traverse(root, None, None)
        
        