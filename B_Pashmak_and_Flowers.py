from collections import Counter
n = int(input())
b = list(map(int, input().split()))

max_num = max(b)
min_num = min(b)
max_diff = max_num - min_num

count = Counter(b)
max_count = count[max_num]
min_count = count[min_num]

if max_num == min_num:
    way = n*(n-1)//2
    
else:
    way = max_count * min_count

print(max_diff, way)