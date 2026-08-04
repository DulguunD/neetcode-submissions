class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))

        cars.sort(reverse=True)

        for car in cars:
            time = ((target-car[0])/car[1])
            if fleets and fleets[-1] >= time:
                continue
            fleets.append(time)
            
        return len(fleets)

     