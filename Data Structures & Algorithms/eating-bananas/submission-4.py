class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        total = sum(piles)
        piles.sort() 

        lower = int(total/h)
        higher = piles[len(piles)-1]
        k = higher
        while lower <= higher:
            avg = int((lower+higher)//2)
            hours = 0
            for pile in piles:
                hour = math.ceil(pile/avg)
                hours += hour
            if hours > h:
                lower = avg + 1
            elif hours <= h:
                k = min(k, avg)
                higher = avg-1

        return k
        