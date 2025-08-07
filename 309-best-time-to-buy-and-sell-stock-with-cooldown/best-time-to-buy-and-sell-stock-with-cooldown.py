class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        buy = [float("-inf")] * n
        sell = [0] * n
        buy[0] = -prices[0]
        
        for i in range(1, n):
            buy[i] = max(sell[i-2] - prices[i],buy[i-1])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[-1]
           
