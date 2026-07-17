class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        max_val = -10001
        for right in range (k-1, len(nums)):
            result.append(max(nums[left:right+1]))
            left += 1
        return result