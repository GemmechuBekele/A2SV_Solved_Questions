from collections import Counter
t = int(input())

for _ in range(t):
    s = input().strip()
    half = s[:len(s)//2]
    
    if len(set(half))==1:
        print("NO")
    else:
        print("YES")