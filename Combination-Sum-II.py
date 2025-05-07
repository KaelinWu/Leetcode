class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        def backtracking(start, new_target, subset):
            if new_target == 0:
                combinations.append(subset[:])
            elif new_target < 0:
                return
            for i in range(start, len(candidates)):
                if i == start or candidates[i] != candidates[i-1]:
                    subset.append(candidates[i])
                    backtracking(i+1, new_target-candidates[i], subset)
                    subset.pop()
                
        backtracking(0,target,[])
        return combinations