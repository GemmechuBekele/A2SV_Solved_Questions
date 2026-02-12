from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #sort string
        sort_s = sorted(s)
        sort_t = sorted(t)

        #count string
        count_s = Counter(s)
        count_t = Counter(t)

        #check validity
        if count_t != count_s:
            return False
        
        #set string
        set_s = set(s)
        set_t = set(t)

        #check validity
        if set_s != set_t:
            return False

        return True
        