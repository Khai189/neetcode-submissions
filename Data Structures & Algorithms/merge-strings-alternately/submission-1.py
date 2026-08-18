class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        w1 = 0
        w2 = 0

        output = []
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1):
                output.append(word1[w1])
                w1+=1
            
            if w2 < len(word2):
                output.append(word2[w2])
                w2+=1
        
        return "".join(output)


