class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  
        cmax = 0  

        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:  # char == '*'
                cmin -= 1  # if '*' acts as ')'
                cmax += 1  # if '*' acts as '('

            # Too many ')' even if all '*' were '('
            if cmax < 0:
                return False

            # We never need open brackets to dip below 0
            cmin = max(cmin, 0)

        return cmin == 0
