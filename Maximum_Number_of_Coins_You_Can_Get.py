class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        n = len(piles)
        repeat_times = n//3
        piles.sort() 
        
        index = n-2
        sum = 0
        for _ in range(repeat_times):
            sum += piles[index]
            index -= 2
        return sum