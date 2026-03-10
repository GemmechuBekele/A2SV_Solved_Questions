class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in parentheses:
                if not stack:return False
                elif stack[-1] != parentheses[char]: return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return stack == []
        
        