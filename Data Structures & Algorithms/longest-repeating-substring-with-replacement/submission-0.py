import collections
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # {X: 2, Y: 2}
        # 
        left = 0
        mp = Counter()
        max_f = 0
        res = 0
        for right in range(len(s)):
            mp[s[right]] += 1
            max_f = max(max_f, mp[s[right]])
            while (right - left + 1) - max_f > k:
                mp[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res