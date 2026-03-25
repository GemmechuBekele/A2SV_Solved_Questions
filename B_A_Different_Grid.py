t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    a = []
    for _ in range(n):
        a.extend(map(int, input().split()))
    if n*m == 1:
        print(-1)
        continue
    b = a[1:]+a[:1]

    index = 0
    for i in range(n):
        newRow = []
        for j in range(m):
            newRow.append(b[index])
            index += 1
        print(*newRow)