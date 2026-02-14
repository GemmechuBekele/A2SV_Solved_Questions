import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = float('inf')

    # length 2
    for i in range(n - 1):
        if s[i] == 'a' and s[i + 1] == 'a':
            ans = 2
            break

    # length 3
    if ans > 2:
        for i in range(n - 2):
            if s[i:i+3].count('a') >= 2:
                ans = 3
                break

    # length 4
    if ans > 3:
        for i in range(n - 3):
            sub = s[i:i+4]
            if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                ans = 4
                break

    # length 7  ← THIS WAS MISSING
    if ans > 4:
        for i in range(n - 6):
            sub = s[i:i+7]
            if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                ans = 7
                break

    print(-1 if ans == float('inf') else ans)

