
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get)
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
                buckets[freq].append(num)
        # print('Buckets: ', buckets)
        result = []
        for i in range(len(buckets)-1, 0, -1):
                result.extend(buckets[i])
                if len(result) >= k:
                        return result[:k]

        # return []
