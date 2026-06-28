from heapq import * 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            y -= x
            if y > 0:
                heapq.heappush_max(stones, y)

        if len(stones) == 0:
            return 0
        return heapq.heappop_max(stones)
