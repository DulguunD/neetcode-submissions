class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        max_val = -10001
        # right = k-1
        for right in range (k-1, len(nums)):
            max_val = max(nums[left:right+1])
            result.append(max_val)
            left += 1
        #     while right-left+1==k:
        #         # print(f"left: {left}, right: {right}, max_val: {max_val}, window: {result}")
        #         max_val = max(nums[left:right+1])
        #         result.append(max_val)
        #         left += 1
        # length = len(nums)    
        # while right < length:
        #     max_val = max(nums[left:right+1])
        #     result.append(max_val)
        #     right += 1
        #     left += 1
            
        return result