n, k = map(int, input().split())
seq = list(map(int, input().split()))

currentSum = sum(seq[:k])

left = 0
minSum = currentSum
result = [minSum, left]

for right in range(k, n):
    currentSum += seq[right]
    currentSum -= seq[left]

    left += 1
    if currentSum < minSum:
        minSum = currentSum
        result.append((minSum, left))
    

print(result[-1][1]+1)
