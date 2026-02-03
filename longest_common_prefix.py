class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for other_word in strs[1:]:
            while not other_word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix