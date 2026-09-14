class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""  


    




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word

        memo = {}

        def dfs(start: int) -> List[str]:
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            res = []
            curr = root

            # Walk the Trie with s[j]
            for j in range(start, len(s)):
                char = s[j]
                if char not in curr.children:
                    break  # Prefix dead end, prune immediately

                curr = curr.children[char]
                if curr.word:
                    sub_sentences = dfs(j + 1)
                    for sub in sub_sentences:
                        if sub:
                            res.append(curr.word + " " + sub)
                        else:
                            res.append(curr.word)

            memo[start] = res
            return res

        return dfs(0)

