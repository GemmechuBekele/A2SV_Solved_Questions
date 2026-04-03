class Solution:
    import bisect

    def possible(self, r, heaters, houses):
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            left = abs(house - heaters[idx-1]) if idx > 0 else float('inf')
            right = abs(heaters[idx] - house) if idx < len(heaters) else float('inf')
            
            if min(left, right) > r:
                return False
        return True
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        l, r = 0, 10**9
        ans = float("inf")
        while l <= r:
            mid = l + (r-l)//2
            if self.possible(mid, heaters, houses):
                ans = mid
                r = mid-1
            else:
                l = mid + 1
        return ans
        