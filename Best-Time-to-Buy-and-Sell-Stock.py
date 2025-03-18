class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        buy = prices[0]
        for p in prices:
            if p < buy:
                buy = p
            diff = max(diff, p - buy)

        return diff
            
           




        