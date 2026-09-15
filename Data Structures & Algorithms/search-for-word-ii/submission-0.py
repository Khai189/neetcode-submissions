class TrieNode():

    def __init__(self):
        self.children = {}
        self.word = None

class Trie():

    def __init__(self):
        self.root = TrieNode()
    
    def _insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.word = word
    




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for word in words:
            trie._insert(word)
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(board), len(board[0])

        curr = trie.root
        output = []
        def dfs(r, c, node):  
            if node.word:
                output.append(node.word)
                node.word = None
                res = True

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in node.children:
                    temp = board[nr][nc]
                    next_node = node.children[temp]

                    board[nr][nc] = "#"
                    dfs(nr, nc, next_node)
                    board[nr][nc] = temp

                    if not next_node.children and not next_node.word:
                        del node.children[temp]
            


        


        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                if char in trie.root.children:
                    first_node = trie.root.children[char]
                    board[r][c] = "#"
                    dfs(r, c, first_node)
                    board[r][c] = char

                    if not first_node.children and not first_node.word:
                        del trie.root.children[char]
        

        return output


        


























            