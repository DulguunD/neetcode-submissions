class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        max_val = -10001
        right = k
        for right in range (len(nums)):
            while right-left+1==k:
                # print(f"left: {left}, right: {right}, max_val: {max_val}, window: {result}")
                max_val = max(nums[left:right+1])
                result.append(max_val)
                left += 1
             
        return result