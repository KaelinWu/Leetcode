class Solution:
    def jump(self, nums: List[int]) -> int:
        left = right = 0
        jumps = 0
        while right < len(nums)-1:
            farthest = 0
            for i in range(left,right+1):
                farthest = max(farthest, nums[i] + i)
            left = right+1
            right = farthest
            print(right)
            jumps+=1
          

        return jumps
        
            

        