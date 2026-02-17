import math
t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))

    current_sum = sum(b)
    missing_sum = s

    set_b = set(b)
    total_sum  = current_sum + missing_sum

    d = 1 + 8*total_sum
    root = math.isqrt(d)

    if root**2 != d:
        print("NO")
        
    else:
        n = (-1 + root)//2

        if len(b) == len(set_b) and max(b) <= n and (n*(n+1))//2 == total_sum :
            print("YES")
        else:
            print("NO")