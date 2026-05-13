from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(list) 
        for num in nums:
            if num in d:
                return True
            else:
                d[num].append(1)
        return False
       