class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
                # print('j: ', j, ", num: ", nums[j], ", res: ", res)
            result.append(product)
            product = 1
        return result