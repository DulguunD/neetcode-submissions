# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        # how far we've explored
        self.level = -1
        def bfs(node: Optional[TreeNode], depth):
            if node:
                if self.level < depth:
                    # new array
                    result.append([])
                    self.level = depth
                result[depth].append(node.val)
                bfs(node.left, depth+1)
                bfs(node.right, depth+1)



        bfs(root, 0)
        
        return result

        