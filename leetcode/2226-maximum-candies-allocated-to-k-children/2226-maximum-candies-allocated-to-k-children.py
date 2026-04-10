class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canServe(m):
            return sum(pile // m for pile in candies) >= k

        lo, hi = 1, max(candies)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if canServe(mid):
                ans = mid      
                lo = mid + 1
            else:
                hi = mid - 1 
        return ans
            