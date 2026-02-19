n = int(input())

segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r, i + 1))  # store original index (1-based)

# Sort by:
# 1) left ascending
# 2) right descending
segments.sort(key=lambda x: (x[0], -x[1]))

max_right = -1
max_index = -1

for l, r, idx in segments:
    if r <= max_right:
        print(idx, max_index)
        sys.exit()
    
    max_right = r
    max_index = idx

print(-1, -1)