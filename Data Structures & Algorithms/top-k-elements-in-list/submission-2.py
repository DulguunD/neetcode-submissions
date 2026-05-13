class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []
        for num in nums:
                if num not in seen:
                        seen[num] = nums.count(num)
        
        # seen = dict(sorted(seen.items()))
        # final = sorted(seen.keys())
        sorted_desc = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        # sorted_arr = sorted(seen.items(), key=lambda item.value(): item[1], reverse=True)
        # print('Seen: ', seen)
        final = list(sorted_desc.keys())
        # return final[:k]
        print(sorted_desc)
        # print(sorted_arr)

        return final[:k]
                
        