class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = []
        if not nums:
            return 0
        ct = 1
        for i, num in enumerate(nums):
            if num-1 == nums[i-1]:
                ct += 1
            elif num == nums[i-1]:
                continue
            else:
                count.append(ct)
                ct = 1
        
        count.append(ct)
        return max(count)


        