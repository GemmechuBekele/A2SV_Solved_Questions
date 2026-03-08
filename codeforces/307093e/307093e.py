from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = defaultdict(int)
left = 0
ans = 0
unique = 0

for right in range(n):
    freq[a[right]] += 1
    if freq[a[right]] == 1:
        unique += 1

    while unique > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            unique -= 1
        left += 1

    ans += right - left + 1

print(ans)