class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, (ROWS * COLS - 1)

        while left <= right:

            mid = left + (right - left) // 2

            # 7 -> 1, mid // ROWS = 7 // 3 = 2 % ROWS = 2
            row = mid // COLS 
            col = mid % COLS
            val =  matrix[row][col]

            if val == target:
                return True
            
            elif val > target:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False