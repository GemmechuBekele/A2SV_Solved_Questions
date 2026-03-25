t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    val = 0
    maxVal = a[-1]

    for k in range(2, n):
        limit = max(a[k], maxVal - a[k])

        i = 0
        j = k - 1

        while i < j:
            if a[i] + a[j] > limit:
                val += j - i
                j -= 1
            else:
                i += 1

    print(val)
