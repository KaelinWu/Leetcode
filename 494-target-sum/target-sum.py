class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            nextdp = defaultdict(int)
            for val,count in dp.items():
                nextdp[val+num] += count
                nextdp[val-num] += count
            dp = nextdp
        return nextdp[target]