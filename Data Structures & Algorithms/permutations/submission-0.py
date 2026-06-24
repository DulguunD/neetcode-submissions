class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        picked = [False for _ in range(len(nums))]

        def recurse(index, path, picked):
            # print('path: ', path, ', index: ', index, ', val: ', nums[index])
            # print('picked: ', picked)
            if len(path) == len(nums):
                # print('Chosen path: ', path)
                result.append(path[:])
                return

            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    path.append(nums[i])
                    recurse(i, path, picked)
                    path.pop()
                    picked[i] = False   

        recurse(0, [], picked)
        
        return result