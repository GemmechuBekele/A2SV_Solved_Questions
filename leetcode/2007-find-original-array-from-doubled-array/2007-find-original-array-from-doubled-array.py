class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        n = len(changed)
        if n % 2 != 0:
            return res
        changed.sort()
        count = Counter(changed)
        for i in range(n):
            num = changed[i]
            if count[num]==0:
                continue
            if count[num*2]==0:
                return []
            res.append(num)
            count[num] -=1
            count[num*2] -=1
        return res
        