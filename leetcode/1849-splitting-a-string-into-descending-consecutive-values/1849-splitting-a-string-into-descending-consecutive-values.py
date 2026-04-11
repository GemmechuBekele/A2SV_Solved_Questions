class Solution:
    def splitString(self, s: str) -> bool:
        for i in range(1, len(s)):
            first = int(s[:i]) 
            
            if self.dfs(s[i:], first):
                return True
        
        return False


    def dfs(self, remaining, prev):
        if not remaining:
            return True
        
        num = 0

        for i in range(len(remaining)):
            num = num * 10 + int(remaining[i])
            
            if num == prev - 1:
                if self.dfs(remaining[i+1:], num):
                    return True

            if num >= prev:
                break
        
        return False
        