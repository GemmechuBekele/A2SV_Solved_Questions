class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        n = len(s)
        for i in range(n):
            last[s[i]] = i

        left = 0
        end = 0
        index = []
        max_index = 0
        for right in range(n):
            end = max(end, last[s[right]])
            if right == end:
                index.append(right-left+1)
                left = right + 1
        
        return index
