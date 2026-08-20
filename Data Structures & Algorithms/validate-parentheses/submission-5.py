class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        para_mp = {")": "(", "}": "{", "]": "["}
        for elem in s:
            print(elem)
            if elem in para_mp:
                if stack and stack[-1] == para_mp[elem]:
                    stack.pop()
                
                else:
                    return False
                
            else:
                stack.append(elem)

        
        return len(stack) == 0