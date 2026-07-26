class Solution:
   
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        index = 0

        # find intersection inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        
        finder = nums[0]

        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
            
        return finder