from collections import defaultdict
import heapq

n, k = map(int, input().split())
arr  = [int(input()) for _ in range(n)]

freq = defaultdict(int)
nums  = []

for i in range(k):
    freq[arr[i]] += 1

for num in freq:
    if freq[num]==1:
        heapq.heappush(nums, -num)
