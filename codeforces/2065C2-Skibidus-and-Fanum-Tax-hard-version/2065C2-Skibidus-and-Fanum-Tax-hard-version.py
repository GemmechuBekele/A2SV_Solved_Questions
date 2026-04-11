import bisect
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort() 

    prev = float("-inf")

    possible = True

    for i in range(n):
        best = float("inf")

        if a[i] >= prev:
            best = a[i]

        target = prev + a[i]
        idx = bisect.bisect_left(b, target)

        if idx < m:
            val = b[idx] - a[i]
            if val >= prev:
                best = min(best, val)

        if best == float("inf"):
            possible = False
            break

        prev = best  

    print("YES" if possible else "NO")