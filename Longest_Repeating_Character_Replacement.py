class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        le = 0
        longest = 0
        occurrence = 0
        count = {}
        n = len(s)
        for ri in range(n):
            count[s[ri]] = count.get(s[ri], 0)+1
            occurrence = max(occurrence, count[s[ri]])
            
            while (ri - le + 1) - occurrence > k:
                count[s[le]] -= 1
                le += 1

            longest = max(longest, ri - le + 1)

        return longest