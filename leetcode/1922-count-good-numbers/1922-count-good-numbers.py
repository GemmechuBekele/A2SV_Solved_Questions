class Solution:
    modulo = 10**9+7
    def power(self, x, n):
        if n== 0:
            return 1
        half = self.power(x, n//2)
        if n % 2 == 0:
            return (half**2)% self.modulo
        else:
            return (x*half**2)% self.modulo

    def countGoodNumbers(self, n: int) -> int:
        even = (n+1)//2
        odd = n//2
        return (self.power(5, even)*self.power(4, odd)) % self.modulo
        