class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False
    

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        root = TrieNode()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
        
            curr.is_end = True

        memo = {}

        def dfs(i: int) -> int:
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]

            res = 1 + dfs(i + 1)

            curr = root
            for j in range(i, len(s)):
                char = s[j]
                if char not in curr.children:
                    break  

                curr = curr.children[char]
                if curr.is_end:
                    res = min(res, dfs(j + 1))

            memo[i] = res
            return res

        return dfs(0)