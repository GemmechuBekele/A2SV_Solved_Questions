n = int(input())

a = list(map(int, input().split()))

a.sort()
d = 1
problem = []
for i in range(n):
    if a[i] >= d:
        problem.append(a[i])
        d += 1

print(len(problem))