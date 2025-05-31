class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,x in enumerate(nums):
            if x > 0:
                break
            if i > 0 and x == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                threesum = x + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append((nums[l],nums[r],x))
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res