class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        Cars = [1, 4, 5] with speed 2, 5, 3, target = 12
        Okay so how do we determine that we'll need 2 car fleets 
        Take a stack where we calculate the speed
        """

        pairs = [(p, s) for p, s in zip(position, speed)]
        
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

