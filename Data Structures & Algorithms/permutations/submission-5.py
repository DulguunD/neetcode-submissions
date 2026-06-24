class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        visited = set()

        def recurse(index, path, visited):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    recurse(i, path, visited)
                    path.pop()
                    visited.remove(i)
        recurse(0, [], visited)
        return result
