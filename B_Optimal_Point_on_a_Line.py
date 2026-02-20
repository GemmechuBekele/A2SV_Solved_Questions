n = int(input())

x = list(map(int, input().split()))

x.sort()

median = x[(n-1)//2]

print(median)