from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # If len is not equal return false
        if len(word1) != len(word2):
            return False

        set_word1 = set(word1)
        set_word2 = set(word2)

        #If set is not equal return false
        if set_word1 != set_word2:
            return False

        #if frequency is not equal return false
        freq_word1 = Counter(word1)
        freq_word2 = Counter(word2)
        if sorted(freq_word1.values()) != sorted(freq_word2.values()):
            return False

        return True