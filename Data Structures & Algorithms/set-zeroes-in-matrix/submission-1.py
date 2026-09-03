class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row_zero = False
        col_zero = False

        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_zero = True
                    
                    if c == 0:
                        col_zero = True
                    
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
        
        if col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        
        
