class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
                if num not in seen:
                        seen[num] = nums.count(num)
        sorted_desc = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
     
 
        return list(sorted_desc.keys())[:k]
                
        