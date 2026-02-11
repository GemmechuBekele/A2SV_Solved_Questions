class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        sum_arr = []
        if num % 3 == 0:
            sum_arr.extend(map(int,[num / 3 -1, num / 3, num / 3 +1]))
        return sum_arr 