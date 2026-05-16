class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # So this is a decision tree with 3 choices
        # We can add, delete, or replace numbers
        # We only need to perform one of these operations when the current strings of the words arent equal
        m, n = len(word1), len(word2)

        dp = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            res = min(dfs(i + 1, j), dfs(i, j + 1))
            res = min(res, dfs(i + 1, j + 1))
            dp[(i, j)] = res+1
            return dp[(i, j)]

        return dfs(0, 0)

