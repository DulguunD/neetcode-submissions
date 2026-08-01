class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pending = []

        result = [0]*len(temperatures)
        # result = []
        for index, temp in enumerate(temperatures):
            print(f"temp: {temp}, index: {index}, pending: {pending}")
            if pending and temp > pending[-1][0]:
                # print(f"")
                print(f"current index: {index}, temperature: {temp}, pending: {pending[-1][1]}, pending temp: {pending[-1][0]}")
                # result[pending[-1][1]] += (index - pending[-1][1])
                # result[pending[-1][1]] += (pending[-1][1])
                # result.append((index - pending[-1][1]))
                # pending.pop()
                while pending and pending[-1][0] < temp:
                    result[pending[-1][1]] += (index - pending[-1][1])
                    pending.pop()
                pending.append((temp, index))
            else:
                pending.append((temp, index))

        return result        