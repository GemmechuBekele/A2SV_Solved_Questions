t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    casino = []
    for _ in range(n):
        le, ri, real = map(int, input().split())
        casino.append((le, ri, real))

    casino.sort(key=lambda x: x[0])

    flag = True
    while flag:
        flag = False
        for le, ri, real in casino:
            if le <= k and k <= ri and k < real:
                k = real
                flag = True
                
    print(k)
