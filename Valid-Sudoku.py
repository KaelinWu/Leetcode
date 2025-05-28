class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        COL = len(board[0])
        ROW = len(board)
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == \.\:
                    continue
                
                box_ind = (row//3)*3+col//3
                if board[row][col] in row_set[col] or board[row][col] in col_set[row] or board[row][col] in box_set[box_ind]:
                    return False
                row_set[col].add(board[row][col])
                col_set[row].add(board[row][col])
                box_set[box_ind].add(board[row][col])
                
        return True