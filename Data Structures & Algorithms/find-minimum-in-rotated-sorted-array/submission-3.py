class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length-1

        while left + 1 < right:
            mid = int((left+right)/2)
            # check if either range has descending order
            if nums[left] > nums[mid]:
                right = mid
                continue
            if nums[mid] > nums[right]:
                left = mid
                continue
            
            # the array is sorted. return nums[left]
            break
        return min(nums[left], nums[right])

        