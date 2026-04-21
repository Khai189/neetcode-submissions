class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        stack = []
        res = [0] * len(temperatures)
        for ind, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append((t, ind))
                
        return res