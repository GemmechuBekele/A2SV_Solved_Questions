class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for s in ransomNote:
            if  s not in magazine:
                return False
            magazine = magazine.replace(s, "", 1)
            
        return True