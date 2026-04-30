t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    _max = max(a)
    count = 0
    for i in a:
        if i == _max:
            count += 1
    print(count)