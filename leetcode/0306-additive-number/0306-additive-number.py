class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i+1, n):
                first_num = num[:i]
                second_num = num[i:j]
                if (first_num.startswith("0")) and len(first_num) > 1 or \
                    (second_num.startswith("0")) and len(second_num) > 1:
                    continue
                if self.backtrack(first_num, second_num, num[j:]):
                    return True
        return False
    def backtrack(self, first_num, second_num, left_S):
        if not left_S:
            return True
        next_num = str(int(first_num) + int(second_num))
        if not left_S.startswith(next_num):
            return False
        return self.backtrack(second_num, next_num, left_S[len(next_num):])