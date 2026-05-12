class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # There's actually a super weird bucket sort solution to this problem

        count = {}
        counts = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            counts[cnt].append(num)
        
        res = []
        for i in range(len(counts)-1, 0, -1):
            for num in counts[i]:
                res.append(num)
                if len(res) == k:
                    return res


