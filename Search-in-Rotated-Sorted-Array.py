class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        res = -1
#45678012
#450123
        while l <= r:
            pivot = (l+r) // 2
            
            if nums[pivot] == target:
                res = pivot
                break

            if nums[pivot] >= nums[l]:
                if target > nums[pivot] or target < nums[l]:
                    l = pivot+1
                else:
                    r = pivot-1
            else:
                if target < nums[pivot] or target > nums[r]:
                    r = pivot-1
                else:
                    l = pivot + 1
        
        return res


      

        