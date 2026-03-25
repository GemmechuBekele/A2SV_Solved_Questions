n = int(input())
def printNum(n):
    if n == 0:
        return
    if n==1:
        print(n, end="")
    else:
        print(n, end=" ")
    printNum(n-1)
printNum(n)