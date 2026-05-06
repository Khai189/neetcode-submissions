class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Initial Thoughts
        # How do we determine if we can reach the word in the first place?
        # We need to determine at point using a multi-source BFS from both the front and end word

        if endWord not in wordList or beginWord == endWord:
            return 0
        
        m = len(wordList[0])
        wordSet = set(wordList)
        beginQ, endQ = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        while beginQ and endQ:
            if len(beginQ) > len(endQ):
                beginQ, endQ = endQ, beginQ
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(beginQ)):
                word = beginQ.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        
                        nei = word[:i] + chr(c) + word[i + 1:]
                        
                        if nei not in wordSet:
                            continue
                        
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        
                        if nei not in fromBegin:
                            fromBegin[nei] = steps+1
                            beginQ.append(nei)
    
        return 0