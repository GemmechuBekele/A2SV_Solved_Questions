t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    if a == a_sorted:
        print(len(a))
    else:
        print(1)