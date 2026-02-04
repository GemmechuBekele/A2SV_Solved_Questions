class Solution:    
    def findUnion(self, a, b):
        
        a.extend(b)
        c= a
        c.sort()
        union = []
        for element in c:
            if element not in union:
                union.append(element)
        return union