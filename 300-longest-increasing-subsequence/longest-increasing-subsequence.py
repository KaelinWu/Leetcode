class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n+1)
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        res = 1
        for val in dp:
            res = max(val,res)
        return res
