class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        def power(x, n):
            if n == 0:
                return 1
            half = power(x, n//2)
            if n % 2 == 0:
                return half**2
            else:
                return x*half**2
        return power(x, n)
        