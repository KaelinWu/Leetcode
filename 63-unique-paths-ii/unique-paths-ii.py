class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 
        for i in range(1,n):
            if obstacleGrid[0][i] != 1 and dp[0][i-1] != 0:
                dp[0][i] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] != 1 and dp[i-1][0] != 0:
                dp[i][0] = 1
        for row in range(1,m):
            for col in range(1,n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                elif dp[row-1][col] == 0 and dp[row][col-1] == 0:
                    dp[row][col] = 0
                elif dp[row][col-1] == 0:
                    dp[row][col] = dp[row-1][col]
                elif dp[row-1][col] == 0:
                    dp[row][col] = dp[row][col-1]
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]
            