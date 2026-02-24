n, m = map(int, input().split())
a = list(map(int, input().split()))

distinct_count = [0]*n
seen = set()
for i in range(n-1, -1, -1):
    if a[i] not in seen:
        seen.add(a[i])
    distinct_count[i] = len(seen)

for _ in range(m):
    li = int(input())
    print(distinct_count[li-1])

