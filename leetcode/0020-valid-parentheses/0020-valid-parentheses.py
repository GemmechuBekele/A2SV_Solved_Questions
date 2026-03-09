class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if stack and stack[-1] == bracket_map[char]: 
                     stack.pop()
                else:
                    return False
        return len(stack) == 0 
sol =Solution()
        