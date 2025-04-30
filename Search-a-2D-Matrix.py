class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix[0])
        
        lower = 0
        upper = len(matrix)-1
        
        pivot = int((upper + lower)/2)
        while lower < upper:
            
         
            if matrix[pivot][n-1] == target:
                return True
            elif matrix[pivot][n-1] > target:
                upper = pivot
                pivot = int((upper + lower)/2)
            else:
                lower = pivot+1
                pivot = int((upper + lower)/2)
        
        

        row = pivot
        print(row)
        lower = 0
        upper = len(matrix[0])-1
        while lower <= upper:
            pivot = int((upper + lower)/2)
            print(pivot)
            if matrix[row][pivot] == target:
                return True
            elif matrix[row][pivot] > target:
                upper = pivot-1
            else:
                lower = pivot+1
        
        return matrix[row][pivot] == target
            