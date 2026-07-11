class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range (len(prices)-1):
            buy = min(buy, prices[i])
            if prices[i+1] > buy:
                temp = prices[i+1]-buy
                # print(f'making profit: {temp} by buying {buy} and selling at {prices[i+1]}')
                profit = max(profit, temp)
        return profit
            

        