class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        xy = 0
        yx = 0

        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy +=1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx +=1

        #calculate total mismatch
        total_mismatch = xy+yx

        if total_mismatch % 2 != 0:
            return -1

        #minimum swap
        min_swap = (xy//2 + yx//2)+(2 if xy % 2==1 else 0)
        return min_swap