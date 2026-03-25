n, m, k = map(int, input().split())
# n = length of array
# m = number of operation
# k = number of query
a = list(map(int, input().split()))
operation = []
freq_query = [0]*(k+1)
result = []
for _ in range(m):
    l, r, d = map(int, input().split())
    operation.append((l-1, r-1, d))
for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    freq_query[x] += 1
    freq_query[y+1] -= 1

    for i in range(1, m):
        freq_query[i] += freq_query[i-1]
    freq_query[:k]
