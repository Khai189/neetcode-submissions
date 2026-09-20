class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])


        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c])
                box = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)
        
        return True