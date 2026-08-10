class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def isAscending(l: List[int]) -> bool:
            if l[0] >= l[-1]:
                return False
            return True
        def isTargetInRange(l: List[int], t:int) -> bool:
            # if range is ascending check if target is within first and last values
            if isAscending(l):
                # print(f"Ascending: {l}")
                if l[0] <= t and l[-1] >= t:
                   return True
            else:
                # print(f"Descending: {l}")
                if l[0] <= t or l[-1] >= t:
                    return True
            return False

        left = 0
        right = len(nums)-1

        while left+1 < right:
            mid = int((left+right)/2)
            # print(f"left: {nums[left:mid+1]}, right: {nums[mid:right+1]}, mid: {nums[mid]}")

            # is mid == target
            if nums[mid] == target:
                return mid

            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
        
            # first range is descending
            if isTargetInRange(nums[left:mid+1], target):
                right = mid
            else:
                left = mid
       
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        
        return -1
            

        