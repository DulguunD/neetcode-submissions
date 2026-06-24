class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        def recurse(index, path, visited):
            result.append(path[:])
            for i in range (index, len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    recurse(i, path, visited)
                    visited.remove(i)
                    path.pop()
        recurse(0, [], visited)
        return result

        