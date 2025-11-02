class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            sell = prices[i]
            maxp = max(sell-buy,maxp)
            if sell < buy:
                buy = sell
        return maxp
