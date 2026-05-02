class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashMap = {
            "0": "+",
            "2": "abc", "3": "def", 
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(i, cur):
            if i >= len(digits):
                res.append("".join(cur.copy()))
                return
            
            for let in hashMap[digits[i]]:
                cur.append(let)
                backtrack(i+1, cur)
                cur.pop()
            
        backtrack(0, [])
        return res

            

            