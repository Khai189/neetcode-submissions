from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        t_freq = Counter(t)
        s_freq = {}

        have, need = 0, len(t_freq)
        res_range = [-1, -1]
        min_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            s_freq[char] = s_freq.get(char, 0) + 1

            if char in t_freq and s_freq[char] == t_freq[char]:
                have += 1

            while have == need:
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    res_range = [left, right]

                left_char = s[left]
                s_freq[left_char] -= 1
                if left_char in t_freq and s_freq[left_char] < t_freq[left_char]:
                    have -= 1
                
                left += 1

        start, end = res_range
        return s[start : end + 1] if min_len != float("inf") else ""

