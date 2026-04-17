from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = defaultdict(int)
distinct = 0
l = 0
r = 0
count = 0
while r < n:
    if freq[a[r]] == 0:
        distinct += 1
    freq[a[r]] += 1

    while distinct > k:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            distinct -= 1
        l += 1

    count += (r - l + 1)

    r += 1

print(count)