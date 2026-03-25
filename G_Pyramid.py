n = int(input())
def pyramid(n, i):
    if i > n:
        return
    spaces = n-i
    stars = 2*i-1
    print(" "*spaces + "*"*stars)
    pyramid(n, i+1)
pyramid(n, 1)