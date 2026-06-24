class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def recurse(index, combinations, currentTarget):
            # print('combinations: ', combinations)
            if currentTarget < 0:
                return
                
            if currentTarget == 0:
                result.append(combinations[:])
            for i in range(index, len(nums)):
                currentTarget -= nums[i]
                combinations.append(nums[i])
                recurse(i, combinations, currentTarget)
                combinations.pop()
                currentTarget += nums[i]
    
        recurse(0, [], target)
        return result
        