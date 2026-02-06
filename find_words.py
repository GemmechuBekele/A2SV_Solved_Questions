from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)  
        total_length = 0

        for word in words:
            word_count = Counter(word)  
            can_form = True
            for c in word_count:
                if word_count[c] > chars_count.get(c, 0):
                    can_form = False
                    break
            
            if can_form:
                total_length += len(word)

        return total_length
