from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        #find frequency of string
        count_freq = Counter(s) #{'e':2, 't':1, 'r':1}

        
        #Sort based frequency
        new_s = ""
        for val, freq in count_freq.most_common():
            while count_freq[val]:
                new_s = new_s + val
                count_freq[val] -= 1
        return new_s