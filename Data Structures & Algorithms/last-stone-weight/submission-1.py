class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            y -= x
            if y > 0:
                stones.append(y)

        if len(stones) == 0:
            return 0
        return stones[0]
