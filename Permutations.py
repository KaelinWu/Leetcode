class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(start, subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                
                return
            for i in range(start, len(nums)+start):
                if nums[i%len(nums)] not in subset:
                    subset.append(nums[i%len(nums)])
                    backtracking(i+1, subset)
                    subset.pop()

        backtracking(0,[])
        return res
