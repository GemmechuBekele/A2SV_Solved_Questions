from functools import cmp_to_key

t = int(input())
for _ in range(t):
    n = int(input())
    adj = [input().strip() for _ in range(n)]
    
    # Comparison function
    def compare(u, v):
        if u < v:
            if adj[u-1][v-1] == '1':
                return -1
            else:
                return 1
        else:
            if adj[u-1][v-1] == '1':
                return 1
            else:
                return -1

    res = list(range(1, n + 1))
    res.sort(key=cmp_to_key(compare))
    
    print(*res)