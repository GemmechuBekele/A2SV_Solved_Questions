t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total_distance = 0
    for i in range(n-1):
        total_distance += abs(a[i]-a[i+1])

    max_reduction = max(abs(a[0]-a[1]), abs(a[n-1] - a[n-2]))

    for i in range(1, n-1):
        current_segment = abs(a[i-1] - a[i]) + abs(a[i] - a[i+1])
        new_segment = abs(a[i-1] - a[i+1])

        reduction = current_segment -  new_segment

        if reduction > max_reduction:
            max_reduction = reduction

    print(total_distance - max_reduction)