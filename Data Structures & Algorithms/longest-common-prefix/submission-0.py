class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = Trie()
        for string in strs:
            trie._insert_word(string)
        
        return trie._search_common_prefix(strs[0])


class Trie():

    def __init__(self):
        self.root = TrieNode()

    def _insert_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr._set_end()
    
    def _search_common_prefix(self, word):
        
        curr = self.root
        cur_word = []
        for char in word:
            if len(curr.children) == 1 and char in curr.children and not curr.is_end:
                cur_word.append(char)
                curr = curr.children[char]
        
            else:
                return "".join(cur_word)
        
        return "".join(cur_word)


class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def _set_end(self):
        self.is_end = True
    


