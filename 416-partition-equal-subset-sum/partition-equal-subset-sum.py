class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums)
        if t % 2:
            return False
        t = t //2
        
        dp = [False] * (t+1)
        dp[0] = True
        for num in nums:
            for i in range(t, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[t]
                
                