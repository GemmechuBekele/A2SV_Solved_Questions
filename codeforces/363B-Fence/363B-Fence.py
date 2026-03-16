# Compute sum of first k planks
currentSum = sum(seq[:k])
minSum = currentSum
minIndex = 0  # starting index of minimum sum (0-based)

# Sliding window
for i in range(1, n - k + 1):
    currentSum = currentSum - seq[i - 1] + seq[i + k - 1]  # slide window
    if currentSum < minSum:
        minSum = currentSum
        minIndex = i

# Output 1-based index
print(minIndex + 1)