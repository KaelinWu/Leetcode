class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = 1
        curmin = 1
        res = float("-inf")
        for num in nums:
            temp = curmax
            curmax = max(num,curmax*num,curmin*num)
            curmin = min(num,temp*num,curmin*num)
            res = max(res,curmax)
        return res
