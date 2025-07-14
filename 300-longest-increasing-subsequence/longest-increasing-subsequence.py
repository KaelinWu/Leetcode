class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        def binary(val):
            l = 0
            r = len(dp)-1
            while l <= r:
                piv = (l+r)//2
                if dp[piv] == val:
                    return
                if dp[piv] > val:
                    r = piv-1
                else:
                    l = piv+1
            dp[l] = val
        
        dp.append(nums[0])
        for i in range(1,len(nums)):
            
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                binary(nums[i])
        
        return len(dp)
        
