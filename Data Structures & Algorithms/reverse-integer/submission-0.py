class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        
        new_int = 0

        while x > 0:
            last_digit = x % 10
            x //=10 
            new_int*=10
            new_int+=last_digit

            print(new_int)

            if new_int > (2**31-1):
                return 0

        return new_int * sign