n = int(input())
v = list(map(int, input().split()))
m = int(input())

prefix = [0]*(n)
prefix[0] = v[0]
for i in range(1, n):
    prefix[i] = prefix[i-1]+v[i]

u = sorted(v)
sorted_prefix = [0]*(n)
sorted_prefix[0] = u[0]
for i in range(1, n):
    sorted_prefix[i] = sorted_prefix[i-1]+u[i]

for _ in range(m):
    q_type, l, r = map(int, input().split())

    l -= 1
    r -= 1

    if q_type == 2:
        if l == 0:
            print(sorted_prefix[r])
        else:
            print(sorted_prefix[r]-sorted_prefix[l-1])
    else:
        if l == 0:
            print(prefix[r])
        else:
            print(prefix[r]-prefix[l-1])
