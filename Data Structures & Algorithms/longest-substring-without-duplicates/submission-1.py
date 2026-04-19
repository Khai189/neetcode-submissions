class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        res = 0
        mpedRes = {}
        # "apolalope"
        for r in range(len(s)):
            if s[r] in mpedRes:
                left = max(mpedRes[s[r]]+1, left)
            # mr["a"] = 0
            mpedRes[s[r]] = r
            # 4
            res = max(res, r-left+1)
            
        return res

