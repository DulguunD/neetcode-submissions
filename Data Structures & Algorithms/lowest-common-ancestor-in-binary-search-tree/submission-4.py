# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        nodes = []
        self.found_q = False
        self.found_p = False
        
        def traverse(node, path):
            if node is None:
                return

            path.append(node)
            if node == p:
                self.found_p = True
                nodes.append(path)

            if node == q:
                self.found_q = True
                nodes.append(path)
            
            if not self.found_q or not self.found_p:
                traverse(node.left, path[:])

            if not self.found_q or not self.found_p:
                traverse(node.right, path[:])

        traverse(root, [])

        # print(f"Nodes: {nodes}")
        for i in range(len(nodes[1])):
            if nodes[1][i] not in nodes[0]:
                return nodes[1][i-1]