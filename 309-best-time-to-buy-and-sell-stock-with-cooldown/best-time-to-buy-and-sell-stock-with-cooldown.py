class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0 
        buy = [0] * n
        sell = [0] * n
        
        buy[0] = -prices[0]

        for i in range(1,n):
            buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])

        return sell[-1]
