n = int(input())
def invertedPyramid(n, i):
    space = n-i
    star = 2*i-1
    if i == 0:
        return
    print(" "*space + "*"*star)
    invertedPyramid(n, i-1)
invertedPyramid(n, i=n)
