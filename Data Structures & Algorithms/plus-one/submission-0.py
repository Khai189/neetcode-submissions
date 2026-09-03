class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            
            else:
                digits[i] = digits[i] + carry
                carry-=1
                break
            


        return digits if not carry else [1] + digits