class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)

        lower = int(sum(piles)/h)
        higher = max(piles)
        k = higher
        while lower <= higher:
            avg = int((lower+higher)//2)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/avg)
            if hours > h:
                lower = avg + 1
            else:
                k = min(k, avg)
                higher = avg-1

        return k
        