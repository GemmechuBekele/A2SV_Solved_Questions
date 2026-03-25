n, k, q = map(int, input().split())
# n = number of recipes
# k = minimum coverage
# q = number of queries
MAX = 200000
diff = [0] * (MAX + 2)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

for i in range(1, MAX + 1):
    diff[i] += diff[i - 1]

good = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    if diff[i] >= k:
        good[i] = 1

pref = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    pref[i] = pref[i - 1] + good[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a - 1])