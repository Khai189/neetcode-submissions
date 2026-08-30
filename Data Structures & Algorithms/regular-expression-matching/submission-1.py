class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n, m = len(s), len(p)
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(2, m + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 2][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i - 2][j]

                    # Case 2: Match 1+ occurrences if preceding char matches s[j-1]
                    if p[i - 2] == s[j - 1] or p[i - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i][j - 1]
                else:
                    # Regular character match or single '.' wildcard
                    if p[i - 1] == s[j - 1] or p[i - 1] == ".":
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]