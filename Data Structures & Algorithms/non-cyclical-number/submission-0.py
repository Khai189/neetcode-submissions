class Solution:
    def isHappy(self, n: int) -> bool:
        
        def cycle(num):
            output = 0
            while num > 0:
                output += (num % 10) ** 2
                num //= 10
            
            return output

        
        visited = set([n])
        while n != 1:
            new_num = cycle(n)
            if new_num == 1:
                return True

            if new_num in visited:
                return False
            
            visited.add(new_num)
            n = new_num

        return True
            
