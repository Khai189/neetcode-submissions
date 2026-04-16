class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We use sets to track seen numbers for rows, columns, and 3x3 blocks
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num == ".":
                    continue
                
                square_idx = (r//3) * 3 + (c//3)

                if (num in rows[r] or 
                    num in cols[c] or 
                    num in squares[square_idx]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[square_idx].add(num)

        return True
                
