class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n
        

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        post = 1
        for i in range(n-1,-1,-1):
            res[i] = res[i] * post
            post = post * nums[i]
        return res
            
            
            
                