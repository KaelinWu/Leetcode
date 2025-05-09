class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_arr = nums[0]

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            max_arr = max(max_arr,curr)

        
        
        return max_arr
                

        