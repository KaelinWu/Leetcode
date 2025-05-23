class Solution:
    def solve(self, board: List[List[str]]) -> None:
        \\\
        Do not return anything, modify board in-place instead.
        \\\
        ROW = len(board)
        COL = len(board[0])
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(row,col):
            if row < 0 or col < 0 or row == ROW or col == COL or board[row][col] != \O\:
                return
            board[row][col] = \*\
            
            for dr, dc in directions:
                dfs(dr+row,dc+col)
        for row in range(ROW):
            dfs(row,0)
            dfs(row,COL-1)
        for col in range(COL):
            dfs(0,col)
            dfs(ROW-1,col)
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == \*\:
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'