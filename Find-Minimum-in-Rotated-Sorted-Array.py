class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r= len(nums)-1

        while l<=r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
            pivot = (l+r) // 2
            res = min(res,nums[pivot])
            if nums[pivot] >= nums[l]:
                l = pivot+1
            else:
                r = pivot-1
            
        return res
