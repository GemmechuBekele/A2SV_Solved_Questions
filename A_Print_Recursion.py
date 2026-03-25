n = int(input())
def printString(n):
    if n == 0:
        return
    print("I love Recursion")
    printString(n-1)
    
printString(n)