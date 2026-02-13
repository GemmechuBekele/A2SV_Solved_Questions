class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

       
        word_split = s.split()
        
        if len(word_split) != len(pattern):
            return False

        s1 = {} #letter
        s2 = {} # word

        for i, j in zip(pattern, word_split):
            if i in s1:
                if s1[i] != j:
                    return False
            if j in s2:
                if s2[j] != i:
                    return False
            
            s1[i] = j
            s2[j] = i  

        return True  