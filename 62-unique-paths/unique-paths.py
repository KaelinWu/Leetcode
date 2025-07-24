class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        aboveRow = [1] * n
        for row in range(1,m):
            currentRow = [1] * n
            for col in range(1,n):
                currentRow[col] = (currentRow[col-1] + aboveRow[col])
            aboveRow = currentRow
        return aboveRow[-1]

            