class Solution:
    def rob(self, nums: List[int]) -> int:
        def steal(arr):
            n = len(arr)
            if len(arr) == 1:
                return arr[0]
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[1],arr[0])
            for i in range(2,n):
                dp[i] = max(arr[i]+dp[i-2], dp[i-1])
            return dp[n-2]
        return max(steal(nums),steal(nums[::-1]))
