import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        count = Counter(nums)
        # print(count)
        # return heapq.heapify(Counter)
        return heapq.nlargest(k, count.keys(), key=count.get)

        # for num in nums:
        #         if num not in seen:
        #                 seen[num] = nums.count(num)
        # sorted_desc = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        # return list(sorted_desc.keys())[:k]
        # return []
                
        