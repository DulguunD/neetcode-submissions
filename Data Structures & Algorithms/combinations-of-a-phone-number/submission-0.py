class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        length = len(digits)

        if length == 0:
            return []
        maps = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", 
        "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def recurse(index: int, path: str):
            # print(f"index: {index}, path: {path}")
            if index == length:
                # print(f"\tadding : {index}, path: {path}")
                result.append(path)
                return
    
            current = digits[index]
            for j in range(len(maps[current])):
                    # print(f"{maps[i]}")
                path += maps[current][j]
                recurse(index+1, path)
                path = path[:-1]
            # for i in range(index, length):
            #     current = digits[i]
            #     for j in range(len(maps[current])):
            #         # print(f"{maps[i]}")
            #         path += maps[current][j]
            #         recurse(i+1, path)
            #         path = path[:-1]

        recurse(0, "")
        return result