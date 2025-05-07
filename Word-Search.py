class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def backtracking(row, col, index):

            if index == len(word):
                return True
            if row < 0 or col < 0 or row == len(board) or col == len(board[row]) or board[row][col] != word[index] or (row,col) in visited:
                return False
            visited.add((row,col))
            res = backtracking(row -1, col, index+1) or backtracking(row +1, col, index+1) or backtracking(row, col-1, index+1) or backtracking(row, col+1, index+1)
            visited.remove((row,col))
            return res
        count = {}
        for c in word:
            count[c] = 1 + count.get(c,0)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for i in range(ROWS):
            for k in range(COLS):
                if backtracking(i,k,0):
                    return True

        return False

            
            

       

        backtracking(0,0,0, set())
        return res == word