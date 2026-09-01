class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        freq = Counter(s)

        seen = set()
        output = []
        start = end = 0
        for char in s:
            if char not in seen:
                seen.add(char)

            freq[char]-=1
            if freq[char] == 0:
                seen.remove(char)

            if len(seen) == 0:
                output.append(end - start + 1)
                start = end + 1
            
            end+=1
        
        return output

            