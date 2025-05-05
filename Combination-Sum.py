class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(new_target, start, subset):
            print(subset,new_target)
            if new_target == 0:
                combinations.append(subset[:])
                return
            if start == len(candidates):
                return
            if new_target >= candidates[start]:
                subset.append(candidates[start])
                backtracking(new_target - candidates[start], start, subset)
                subset.pop()
            backtracking(new_target, start+1, subset)
               
            

        backtracking(target,0,[])
        return combinations