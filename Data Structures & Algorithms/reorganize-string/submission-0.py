class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        
        sorted_chars = sorted(counts.keys(), key=lambda c: counts[c], reverse=True)
        
        if counts[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""
        
        res = [''] * len(s)
        idx = 0
        
        for char in sorted_chars:
            for _ in range(counts[char]):
                if idx >= len(s):
                    idx = 1
                res[idx] = char
                idx += 2
                
        return "".join(res)