n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
i = j = 0
ans = 0
 
while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        x = a[i]
        ca = 0
        cb = 0
 
        while i < n and a[i] == x:
            ca += 1
            i += 1
        while j < m and b[j] == x:
            cb += 1
            j += 1
 
        ans += ca * cb
 
print(ans)