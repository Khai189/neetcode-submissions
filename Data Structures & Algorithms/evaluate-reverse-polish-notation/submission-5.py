class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                second_elem = stack.pop()
                first_elem = stack.pop()

                if token == "+":
                    stack.append(first_elem + second_elem)
                
                elif token == "-":
                    stack.append(first_elem - second_elem)
                
                elif token == "*":
                    stack.append(first_elem * second_elem)
                
                else:
                    stack.append(int(first_elem / second_elem))
            
            else:
                stack.append(int(token))
        
        return stack[-1]