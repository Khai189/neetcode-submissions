class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # This is a decision tree with 2 choices at each poin
        # Do we add a letter from s1 or do we add a letter from s2?
        # This has a couple edge cases
        # Number one, we can try making this into a tree problem
        # At each point in the tree, we try to add a letter from either a or b
        # This however results in quite a bit of time
        # O(2^n), which is incredibly slow
        # We try a dynamic programming approach
        # We are doing a TON of recalculating at each point
        # We can do a bottom-up approach where for each word in s3 we try to see if a or b can currently add to it
        # We'll use a hashmap to host the current outcomes we already have
        
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            ans = False
            
            if i < len(s1) and s1[i] == s3[i + j]:
                ans = ans or dfs(i+1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                ans = ans or dfs(i, j+1)
            
            dp[(i, j)] = ans
            return dp[(i, j)]
        return dfs(0, 0)

        