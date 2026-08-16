class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]

                if val == ".":
                    continue
                
                num = int(val)

                box = (r // 3) * 3 + (c // 3)
                print(r, c)
                print(box)

                if num in rows[r] or num in cols[c] or num in boxes[box]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        
        return True