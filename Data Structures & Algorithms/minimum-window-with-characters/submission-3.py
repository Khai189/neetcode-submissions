from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        elif len(s) < len(t):
            return ""

        mp = Counter(t)
        mpFreq = {}
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(mp)
        # YAXHLOPSOXHAP, look for HP
        left = 0
        for r in range(len(s)):
            c = s[r]
            mpFreq[c] = 1 + mpFreq.get(c, 0)
            if c in mp and mpFreq[c] == mp[c]:
                have+=1
            
            while have == need:
                if (r - left + 1) < resLen:
                    res = [left, r]
                    resLen = r - left + 1

                mpFreq[s[left]] -=1
                if s[left] in mp and mpFreq[s[left]] < mp[s[left]]:
                    have-=1
                left+=1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                 
 

           
            