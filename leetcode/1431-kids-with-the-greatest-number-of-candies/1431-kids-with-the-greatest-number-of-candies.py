class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        bool_arr = []
        for candy in candies:
            if candy + extraCandies < max_candies:
                bool_arr.append(False)
            else:bool_arr.append(True)
        return bool_arr