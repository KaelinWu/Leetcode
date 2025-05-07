class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        nums.sort()

        def backtracking(start,subset):
           
            if start == len(nums):
                power_set.append(subset[:])
                return
            subset.append(nums[start])
            backtracking(start+1,subset)
            subset.pop()
            while start < len(nums)-1 and nums[start] == nums[start+1]:
                start+=1
            backtracking(start + 1, subset)


        backtracking(0,[])
        return power_set
            
                
        