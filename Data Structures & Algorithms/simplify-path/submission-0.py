class Solution:
    def simplifyPath(self, path: str) -> str:
        # unix style file system which begins with a /
        # Turn it simpler
        # . means we are in the current directory
        # .. means the previous parent directory
        # / represents a single slash

        
        stack = []
        paths = path.split("/")

        for cur in paths:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)

        return "/" + "/".join(stack)