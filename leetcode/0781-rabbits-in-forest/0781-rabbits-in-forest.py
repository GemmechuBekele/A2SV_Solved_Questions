class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0

        for x, c in count.items():
            group = x + 1
            groups = math.ceil(c / group)
            total += groups * group

        return total
            