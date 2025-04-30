class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        max_buy = 0
        for i in range(len(prices)):
            new_buy = prices[i] - prices[buy_index]
            if new_buy < 0:
                buy_index = i
            elif new_buy > max_buy:
                max_buy = new_buy
            
        return max_buy