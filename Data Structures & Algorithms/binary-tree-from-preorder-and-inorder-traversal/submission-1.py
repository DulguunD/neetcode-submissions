# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        self.index = 0
        for index, value in enumerate(inorder):
            inorder_map[value] = index

        def build(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None

            root_value = preorder[self.index]
            self.index += 1
            root_index = inorder_map[root_value]
            node = TreeNode(root_value)

            # print(f"Inorder: {inorder_left} - {inorder_right}")

            node.left = build(inorder_left, root_index-1)
            node.right = build(root_index+1, inorder_right)

            return node

        return build(0, len(preorder)-1)
        