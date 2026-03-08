n, q = map(int, input().split())
a = list(map(int, input().split()))

freq = [0]*(n+1)
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    freq[l] += 1
    freq[r+1] -= 1

for i in range(1,n):
    freq[i] += freq[i-1]

freq = freq[:n]

sorted_freq = sorted(freq)
sorted_arr = sorted(a)
ans = 0
for i in range(n):
    ans += (sorted_arr[i]*sorted_freq[i])

print(ans)