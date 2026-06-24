class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        # picked = [False for _ in range(n)]
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
                # if not picked[i]:
                #     picked[i] = True
                #     path.append(nums[i])
                #     recurse(i, path, picked)
                #     path.pop()
                #     picked[i] = False   

        recurse(0, [], visited)
        return result
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     n = len(nums)
    #     picked = [False for _ in range(n)]

    #     def recurse(index, path, picked):
    #         if len(path) == len(nums):
    #             result.append(path[:])
    #             return
    #         for i in range(n):
    #             if not picked[i]:
    #                 picked[i] = True
    #                 path.append(nums[i])
    #                 recurse(i, path, picked)
    #                 path.pop()
    #                 picked[i] = False   

    #     recurse(0, [], picked)
    #     return result