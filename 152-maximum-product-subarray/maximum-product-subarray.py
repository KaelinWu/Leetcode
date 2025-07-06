class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsub = 1
        maxsub = 1
        res = float("-inf")
        for num in nums:
            temp = maxsub
            maxsub = max(num,maxsub*num,num*minsub)
            minsub = min(num,temp*num,num*minsub)
            res = max(res,maxsub)
        return res