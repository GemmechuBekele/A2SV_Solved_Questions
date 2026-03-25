class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for p in logs:
            if p == "../":
                if stack:
                    stack.pop()
            elif p == "./":
                continue
            else:
                stack.append(p)
                
        return len(stack)
        