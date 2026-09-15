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

            # path.append(node.val)
            path.append(node)
            if node == p:
                nodes.append(path)
                self.found_p = True
                # print(f"FOUND p: current path: {path}")

            if node == q:
                # print(f"FOUND q: current path: {path}")
                self.found_q = True
                nodes.append(path)
            
            if not self.found_q or not self.found_p:
                traverse(node.left, path[:])

            if not self.found_q or not self.found_p:
                traverse(node.right, path[:])

        traverse(root, [])

        # print(f"Nodes: {nodes}")

        # res = [x for x in nodes[0] if x in nodes[1]]
        # for x in nodes[0]:
        #     if x in nodes[1]:
        #         return TreeNode(x)
        for i in range(len(nodes[1])):
            if nodes[1][i] not in nodes[0]:
                return nodes[1][i-1]