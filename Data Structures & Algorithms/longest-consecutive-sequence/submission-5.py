class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = set()
        nums.sort()
        print('nums: ', nums)
        count = []
        ct = 1
        if not nums:
            return 0
        for i, num in enumerate(nums):
            start.add(num)
            if num-1 == nums[i-1]:
                # start.add(num)
                ct += 1
            elif num == nums[i-1]:
                continue
            else:
                count.append(ct)
                ct = 1
        
        count.append(ct)

        # print(f"start: {start}")  
        print(f"count: {count}")
        return max(count)


        