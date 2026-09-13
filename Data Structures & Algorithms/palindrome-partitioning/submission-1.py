class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        def expand(l: int, r: int):
            while l >= 0 and r < n and s[l] == s[r]:
                is_pal[l][r] = True
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        res = []
        path = []

        def backtrack(start: int):
            if start == n:
                res.append(path.copy())
                return

            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res