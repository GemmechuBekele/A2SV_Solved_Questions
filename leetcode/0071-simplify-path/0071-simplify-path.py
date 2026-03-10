class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split = path.split("/")

        stack = []
        for p in path_split:
            if p == "." or p == "":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
                
        result = "/"+"/".join(stack)
        return result
        