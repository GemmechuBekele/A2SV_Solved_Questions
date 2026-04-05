class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)#{'e':3, 'l':1, 't':1, 'c':1, 'o':1, 'd':1}
        c2 = Counter(t) #{'c': 2, 'p':1, 'a':1, 'r':1, 't':1, 'i':1, 'e':1}
        a = 0
        for c in c2:
            
            if c1[c] < c2[c]:
                 a = a+(c2[c]-c1[c])
              
        return a


        