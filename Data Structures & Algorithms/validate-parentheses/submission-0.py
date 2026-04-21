class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validOptions = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c in validOptions:
                if stack and stack[-1] == validOptions[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return stack == []
        