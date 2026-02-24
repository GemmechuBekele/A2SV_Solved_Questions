class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        le = 0
        
        while le <= len(haystack) - len(needle):
            word = ""
            ri = le
            
            while ri < le + len(needle) and haystack[ri] == needle[ri - le]:
                word += haystack[ri]
                ri += 1
            
            if word == needle:
                return le
            
            le += 1
        
        return -1
        