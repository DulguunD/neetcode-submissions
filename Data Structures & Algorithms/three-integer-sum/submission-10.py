class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        start, end = 0, len(nums)-1
        mid = 1
        nums.sort()
        length = len(nums)-1

        while mid < end:
            total = nums[start]+nums[mid]+nums[end]
            if total < 0:
                start += 1
                if mid==start:
                    end = length
                    mid += 1
                    start = 0
                continue
            elif total > 0:
                end -= 1
                if mid==end:
                    start = 0
                    mid += 1
                    end = length
                continue
            else:
                temp = [nums[start], nums[mid], nums[end]]
                if temp not in result:
                    result.append(temp)        
                start += 1
                if mid==start:
                    end = length
                    mid += 1
                    start = 0

        return result
        