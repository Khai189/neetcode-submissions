class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [0] * (m + 1)
        dp[0] = 1  # Base case: 1 way to make an empty string
        
        for char_s in s:
            for j in range(m, 0, -1):
                if char_s == t[j-1]:
                    dp[j] += dp[j-1]
                    
        return dp[m]