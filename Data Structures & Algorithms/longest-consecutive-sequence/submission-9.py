class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = []
        if not nums:
            return 0
        ct = 1
        length = len(nums)
        for i in range(length):
            if nums[i]-1 == nums[i-1]:
                ct += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                count.append(ct)
                ct = 1
        
        count.append(ct)
        return max(count)


        