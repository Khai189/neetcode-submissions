class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []

        def backtrack(rem_open, rem_close, path):
            if rem_open == rem_close == 0:
                output.append("".join(path))
                return
            
            if rem_open < rem_close:
                path.append(")")
                backtrack(rem_open, rem_close-1, path)
                path.pop()
            
            if rem_open > 0:
                path.append("(")
                backtrack(rem_open-1, rem_close, path)
                path.pop()

        backtrack(n, n, [])
        return output


