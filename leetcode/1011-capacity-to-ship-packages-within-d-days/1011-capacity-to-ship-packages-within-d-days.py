class Solution:
    def possible(self, cap, weights, days):
        day = 1
        load = 0
        for w in weights:
            if w > cap:
                return False
            if load + w <= cap:
                load += w
            else:
                day += 1
                load = w
        return day <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = float("inf")
        while l <= r:
            mid = (l+r)//2
            if self.possible(mid, weights, days):
                ans = mid
                r = mid-1
            else:
                l = mid + 1
        return ans
    
        