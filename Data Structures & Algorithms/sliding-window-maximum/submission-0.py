class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        left = 0
        window = []
        max_val = -10001
        s = k
        right = k
        for right, num in enumerate(nums):
            window.append(num)
            while right-left+1==k:
                # print(f"left: {left}, right: {right}, max_val: {max_val}, window: {result}")
                max_val = max(nums[left:right+1])
                result.append(max_val)
                left += 1
             
        return result