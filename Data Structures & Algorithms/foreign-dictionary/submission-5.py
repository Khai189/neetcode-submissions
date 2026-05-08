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
        graph= defaultdict(set)
        indegree = {c:0 for i in words for c in i }

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
    
            minLength = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j]!=w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break   


        topo= []
        ans = ""
        for i in indegree:
            if indegree[i]==0:
                topo.append(i)

        while topo:
            letter = topo.pop(-1)
            ans+=letter

            for nei in graph[letter]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    topo.append(nei)

        return ans if len(ans)==len(indegree) else  ""

