class Solution:
    def findValidPair(self, s: str) -> str:

        dict_s = {}

        for i in s:
            dict_s[i] = dict_s.get(i, 0)+1

        for j in range(len(s)-1):
            a = s[j]
            b = s[j+1]

            if a != b and int(a) == dict_s[a] and int(b) == dict_s[b]:
                return a+b
        
        else:
            return ""
        
sol = Solution()
print(sol.findValidPair('1522'))