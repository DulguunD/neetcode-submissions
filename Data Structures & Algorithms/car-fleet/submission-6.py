class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = []
        counter = 0
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(reverse=True)
        for i in range(len(cars)):
            # print(f"Index: {i}")
            time = ((target-cars[i][0])/cars[i][1])
            if fleets and fleets[-1] >= time:
                counter += 1
            else:
                fleets.append(time)

        return len(fleets)

     