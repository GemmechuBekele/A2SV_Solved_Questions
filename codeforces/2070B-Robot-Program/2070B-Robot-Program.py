t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    pref = [0] * (n + 1)

    for i in range(n):
        if s[i] == 'L':
            pref[i+1] = pref[i] - 1
        else:
            pref[i+1] = pref[i] + 1

    first_time = -1
    for i in range(1, n+1):
        if x + pref[i] == 0:
            first_time = i
            break

    if first_time == -1 or first_time > k:
        print(0)
        continue

    cycle = -1
    for i in range(1, n+1):
        if pref[i] == 0:
            cycle = i
            break

    if cycle == -1:
        print(1)
    else:
        remaining = k - first_time
        print(1 + remaining // cycle)