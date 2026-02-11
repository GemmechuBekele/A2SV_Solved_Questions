from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        non_dup = []
        for arr in responses:
            count = Counter(arr)
            for val in count:
                non_dup.append(val)

        set_list = Counter(non_dup)

        #find max frequency
        max_freq = max(set_list.values())

        candidate = [word for word, freq in set_list.items() if freq == max_freq ]

        #return lexicographically smallest among candidates
        return min(candidate)