class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        nums.sort()
        def recurse(index, path):
            if path not in result:
                result.append(path[:])
            for i in range(index, len(nums)):
                if i not in seen:
                    seen.add(i)
                    path.append(nums[i])
                    # print(f"Index: {i}, Value: {nums[i]}, Path: {path}")
                    recurse(i, path)
                    seen.remove(i)
                    path.pop()
        recurse(0, [])
        return result
        