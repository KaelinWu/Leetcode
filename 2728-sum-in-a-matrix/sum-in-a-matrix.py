class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        rows = [sorted(row) for row in nums]
        res = 0
        for i in range(len(rows[0])):
            add = 0
            for row in rows:
                add = max(add,row[i])
            res+=add
        return res
