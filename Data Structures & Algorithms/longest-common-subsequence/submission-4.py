class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        n, m = len(text1), len(text2)
        prev = [0] * (m + 1)

        for i in range(n):
            curr = [0] * (m + 1)
            for j in range(m):
                if text1[i] == text2[j]:
                    curr[j + 1] = 1 + prev[j]
                else:
                    curr[j + 1] = max(prev[j + 1], curr[j])
            prev = curr

        return prev[m]

                 