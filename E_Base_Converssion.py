t = int(input())
for _ in range(t):
    n = int(input())
    def convertToBinary(n):
        if n==0:
            return
        convertToBinary(n//2)
        print(n % 2, end="")

    if n == 0:
        print(0)
    else:
        convertToBinary(n)
        print()