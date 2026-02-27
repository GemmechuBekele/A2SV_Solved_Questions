class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        le = 0
        ri = int(sqrt(c))
        flag = False
        while le <= ri:
            if (le**2 + ri**2) < c:
                le += 1
            elif (le**2 + ri**2) > c:
                ri -= 1
            else:
                flag = True
                return flag

        return flag