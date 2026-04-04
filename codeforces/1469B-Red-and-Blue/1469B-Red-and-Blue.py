t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    
    redPrefix = [0]*n
    redPrefix[0] = r[0]
    for i in range(1, n):
        redPrefix[i] = redPrefix[i-1] + r[i]
    
    bluePrefix = [0]*m
    bluePrefix[0] = b[0]
    for j in range(1, m):
        bluePrefix[j] = bluePrefix[j-1] + b[j]

    redMax = 0
    blueMax = 0
    redMax = max(redMax, max(redPrefix))
    blueMax = max(blueMax, max(bluePrefix))

    total = redMax + blueMax
    print(total)