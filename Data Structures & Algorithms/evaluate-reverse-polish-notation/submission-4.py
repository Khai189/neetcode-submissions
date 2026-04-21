class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                int2 = stack.pop()
                int1 = stack.pop()
                res = 0
                match token:
                    case "+":
                        res = int1 + int2
                    case "-":
                        res = int1 - int2
                    case "*":
                        res = int1 * int2
                    case "/":
                        # dont need to account for 0, must be valid
                        res = int(int1 / int2)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]