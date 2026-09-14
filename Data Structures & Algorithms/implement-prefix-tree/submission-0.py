class TrieNode():

    def __init__(self):
        self.children = {}
        self.is_end = False
    

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.is_end
        
    
    def search_all_children(self, node: TrieNode) -> bool:
        if node.is_end:
            return True

        curr = node

        for child in curr.children:
            if self.search_all_children(curr.children[child]):
                return True
        
        return False



    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return self.search_all_children(curr)

        
        