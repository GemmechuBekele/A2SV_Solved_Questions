# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# n version, [1, 2, 3, 4, 5]
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l , r = 1, n
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid):
                ans = mid
                r = mid-1
            else:
                l = mid + 1
        return ans