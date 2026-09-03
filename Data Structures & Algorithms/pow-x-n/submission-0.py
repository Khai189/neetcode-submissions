class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1 / x
            n = -n

        def helper(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0
            
            if exp % 2 == 1:
                return base * helper(base * base, exp // 2)
            
            return helper(base * base, exp // 2)

        return helper(x, n)
