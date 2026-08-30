class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n, m = len(word1), len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                
                else:
                    replace = 1 + dp[i][j]
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]

                    dp[i+1][j+1] = min(replace, insert, delete)

        return dp[n][m]