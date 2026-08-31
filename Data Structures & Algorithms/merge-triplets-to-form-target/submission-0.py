class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        cur = [0, 0, 0]

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                cur[0] = max(cur[0], a)
                cur[1] = max(cur[1], b)
                cur[2] = max(cur[2], c)

        return cur == target