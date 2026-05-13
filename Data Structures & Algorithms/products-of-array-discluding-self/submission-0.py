class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        res = 1
        i = 1
        for i, num in enumerate(nums):
            # res *= num
            # print('i: ', i, ", num: ", num, ", res: ", res)
            for j in range(len(nums)):
                if i != j:
                    res *= nums[j]
                # print('j: ', j, ", num: ", nums[j], ", res: ", res)
            result.append(res)
            res = 1

        return result