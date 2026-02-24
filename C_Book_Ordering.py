n = int(input())

prev = float('inf')
flag = "YES"

for _ in range(n):
    w, h = map(int, input().split())
    
    big = max(w, h)
    small = min(w, h)
    
    if big <= prev:
        prev = big
    elif small <= prev:
        prev = small
    else:
        flag = "NO"

print(flag)