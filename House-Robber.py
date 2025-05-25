class Solution:

    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n ==0:
            return 0
        elif n ==1:
            return nums[0]
        memo = [-1] * n
        memo[0] = nums[0]
        memo[1] = max(memo[0],nums[1])
        for i in range(2,n):
            memo[i] = max(memo[i-2]+nums[i],memo[i-1])
        return memo[n-1]
        
        