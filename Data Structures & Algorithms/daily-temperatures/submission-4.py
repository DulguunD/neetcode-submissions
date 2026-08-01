class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pending = []
        result = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            # print(f"temp: {temp}, index: {index}, pending: {pending}")
            while pending and pending[-1][0] < temp:
                result[pending[-1][1]] += (index - pending[-1][1])
                pending.pop()
            pending.append((temp, index))
        return result        