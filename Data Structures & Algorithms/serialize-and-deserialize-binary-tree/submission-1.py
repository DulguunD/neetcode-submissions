# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node):
            nonlocal result
            if not node:
                result.append("x")
                return 
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        res = " ".join(map(str, result))
        # print(f"serialized: {res}")
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        length = len(data)-1
        # print(f"Data to deserialize: {data}, length: {length}")
        index = 0

        def build(startIndex: int):
            nonlocal length
            if startIndex > length:
                return None

            nonlocal index
            root_value = None

            while data[index].isspace():
                index += 1
            
            if data[index] == "x":
                index +=1 
                return None
            else:
                start = index
                while not data[index].isspace():
                    index += 1
                root_value = int(data[start:index+1])
            
            node = TreeNode(root_value)
            node.left = build(index)
            node.right = build(index+1)
            return node

        result = build(0)
        return result
