class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        total = sum(piles)
        average = int(total/h)

        piles.sort() 

        lower = average
        higher = piles[len(piles)-1]

        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        # print(f"Piles Sorted: {piles}")
        avg = 0
        minimum = higher
        while lower <= higher:
            avg = int((lower+higher)//2)
            # print(f"avg: {avg}, lower: {lower}, higher: {higher}")
            hours = 0
            for pile in piles:
                hour = math.ceil(pile/avg)
                hours += hour
            # minimum = min(minimum, avg)
            # print(f"Pile: {pile}, hour: {hour}, minimum: {minimum}")
            # print(f"Total Hours: {hours}, with avg: {avg}, mini: {minimum}")
            if hours > h:
                # increase 
                lower = avg + 1
            elif hours <= h:
                # print(f"OPtimal: {avg}")
                minimum = min(minimum, avg)
                higher = avg-1
                # 
            
        
        # print(f"* * Lower: {lower}, higher: {higher}, avg: {avg}")
        # print(f"Average should be around: {average}")

        return minimum
        