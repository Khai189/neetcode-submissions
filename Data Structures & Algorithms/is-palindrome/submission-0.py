class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        newS = "".join(char.lower() for char in s if char.isalnum())
        right = len(newS)-1
        while left < right:
            if newS[left] != newS[right]:
                return False
            else:
                left +=1
                right -=1
        return True

        