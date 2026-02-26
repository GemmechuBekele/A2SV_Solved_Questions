t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd_count = 0
    even_count = 0

    for i in range(n):
        if a[i] % 2 == 1:
            odd_count += 1
        else:
            even_count += 1

    if odd_count % 2 == 1:
        print("YES")
    elif even_count > 0 and odd_count > 0:
        print("YES")
    else:
        print("NO")