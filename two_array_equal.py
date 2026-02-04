class Solution:
    def checkEqual(self, a, b):
        if len(a) != len(b):
            return False
        
        a.sort()
        b.sort()
        
        return a == b