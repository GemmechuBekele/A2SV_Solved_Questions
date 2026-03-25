n, s = map(int, input().split())
a = list(map(int, input().split()))
 
left = 0
current_sum = 0
ans = 0
 
for right in range(n):
    current_sum += a[right]
 
    while current_sum > s:
        current_sum -= a[left]
        left += 1
 
    ans += right - left + 1
 
print(ans)