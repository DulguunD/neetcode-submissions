class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        length = len(digits)

        if length == 0:
            return []

        maps = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", 
        "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def recurse(index: int, path: str):
            if index == length:
                result.append(path)
                return
            current = digits[index]
            for j in range(len(maps[current])):
                path += maps[current][j]
                recurse(index+1, path)
                path = path[:-1]
          
        recurse(0, "")
        return result