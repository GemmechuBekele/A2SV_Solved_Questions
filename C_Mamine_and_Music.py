n, k = map(int, input().split())

a = list(map(int, input().split()))

inst = [(a[i], i+1) for i in range(n)]

inst.sort()
tot = 0
see  = []
for d, ix in inst:
    if tot + d <=k:
        tot+=d
        see.append(ix)
    else:
        break
print(len(see))
print(*see)