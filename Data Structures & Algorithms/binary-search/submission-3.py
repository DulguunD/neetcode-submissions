class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = len(nums)/2
        counter = 100
        while left <= right:
            # counter -= 1
            mid = int((left+right)/2)
            # print(f"left: {left}, right: {right}, mid: {mid}")
            if nums[mid] < target:
                left = mid+1
                continue
            elif nums[mid] > target:
                right = mid-1
                continue
            else:
                return mid
        # print(f"left: {left}, right: {right}, mid: {mid}")
        
        return -1    
