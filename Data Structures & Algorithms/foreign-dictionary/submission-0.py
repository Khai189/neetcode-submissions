class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # So, first we need to start out with what is this problem
        # We're taking a list of words and trying to figure out the order in the letters
        # Let's think about edge cases: can there be duplicate letters in a row? aka tt or zz etc
        # We know the words are already sorted
        # What does it mean to have no solution? Would it mean that, for example "rt" and "tr" would have no solution?
        # We also know there's no solution if a prefix such as apes coming before ape that means no solution
        # Essentially, we can think of this as a graph, however in a different way
        # These words are essentially nodes inside of the graph
        adj = {c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            minLen = min(len(w1), len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        return "".join(res[::-1])

