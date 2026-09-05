# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        def traverse(node: TreeNode, minNum: int, maxNum: int):
            if not node:
                return
            if minNum is not None and node.val <= minNum:
                self.valid = False
                return
            if maxNum is not None and node.val >= maxNum:
                self.valid = False
                return

            # left side
            leftMin = minNum
            leftMax = node.val
            traverse(node.left, leftMin, leftMax)

            #right side
            if maxNum is not None:
                rightMax = max(maxNum, node.val)
            else:
                rightMax = maxNum
        
            rightMin = node.val
            traverse(node.right, rightMin, rightMax)

        traverse(root, None, None)
        return self.valid
        
        