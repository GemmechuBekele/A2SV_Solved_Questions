n = int(input())

def factorial(n):
    if n == 0:
        return
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))