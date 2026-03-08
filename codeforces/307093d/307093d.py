n, s = map(int, input().split())
a = list(map(int, input().split()))

left = 0
cur = 0
ans = 0

for right in range(n):
    cur += a[right]
    
    while cur >= s:
        ans += n - right
        cur -= a[left]
        left += 1

print(ans)