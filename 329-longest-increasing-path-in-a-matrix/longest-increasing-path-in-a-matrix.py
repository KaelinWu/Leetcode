class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW,COL = len(matrix),len(matrix[0])
        dp = defaultdict()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(row,col,prev):
            if row < 0 or col < 0 or row >= ROW or col >= COL or matrix[row][col] <= prev:
                return 0
            if (row,col) in dp:
                return dp[(row,col)]
            ret = 1
            for dr,dc in directions:
                ret = max(ret, 1 + dfs(row+dr,col+dc,matrix[row][col]))
            dp[(row,col)] = ret
            return ret
        for row in range(ROW):
            for col in range(COL):
                dfs(row,col,-1)
        return max(dp.values())