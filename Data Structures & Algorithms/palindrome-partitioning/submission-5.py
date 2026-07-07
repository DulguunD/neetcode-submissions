class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        length = len(s)
        def isPalindrome(path: str):
            if path and path == path[::-1]:
                return True
            return False

        def backtrack(currentIndex, path, splits):
            if currentIndex > length:
                return
            if splits and currentIndex == length and splits not in res:
                res.append(splits[:])
                return
            
            for i in range(currentIndex, length):
                path += s[i]
                if isPalindrome(path):
                    splits.append(path)
                    backtrack(i+1, '', splits)
                    splits.pop()
                else:
                    continue
        backtrack(0, "", [])
        return res
        