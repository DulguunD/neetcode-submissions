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
            # print(f'CurrentIndex: {currentIndex}, path: {path}, sp: {splits}')

            # if sum(len(splits)) == length and splits not in res:
            #     res.append(splits[:])
            #     return

            if splits and currentIndex == length and splits not in res:
                # print(f'\tadding to the result: {splits}, path: {path}')
                res.append(splits[:])
                # print(f'splits: {splits}')
                return
            
            for i in range(currentIndex, length):
                # print(f'i: {i}, path: {path}, splits: {splits}')
                path += s[i]
                if isPalindrome(path):
                    splits.append(path)
                    backtrack(i+1, '', splits)
                    splits.pop()
                    # path = ''
                else:
                    continue
                    # backtrack(i+1, path, splits)
                    # path = path[-1]
                    # path = ''
                # splits.append(path)
                # backtrack(i+1, path, splits)
                # path = path[-1]
                # splits.pop()
                # path += s[i]
                # backtrack(i+1, path, splits)
                # path = path[-1]

        backtrack(0, "", [])

        return res
        