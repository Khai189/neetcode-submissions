class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev_row = [0] * (n+1)
        prev_row[0] = 1
        for i in range(m):
            cur_row = [0] * (n+1)
            for j in range(n):
                if j == 0:
                    cur_row[j] = prev_row[j]
                cur_row[j] = prev_row[j] + cur_row[j-1]
        
            prev_row = cur_row
        
        return prev_row[-2]