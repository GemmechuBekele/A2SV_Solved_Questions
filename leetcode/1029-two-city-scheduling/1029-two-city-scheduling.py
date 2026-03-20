class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    # Sort based on difference (A - B)
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2
        total = 0

        # First n → City A
        for i in range(n):
            total += costs[i][0]

        # Last n → City B
        for i in range(n, 2*n):
            total += costs[i][1]

        return total