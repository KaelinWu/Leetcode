class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        nums = nums[::-1]
        dp2 = [0] * n
        dp2[0] = nums[0]
        dp2[1] = max(nums[1],nums[0])
        for i in range(2,n):
            dp2[i] = max(nums[i]+dp2[i-2], dp2[i-1])
        return max(dp[n-2],dp2[n-2])
