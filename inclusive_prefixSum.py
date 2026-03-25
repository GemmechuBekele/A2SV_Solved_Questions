def prefixSum(nums):
    n = len(nums)
    acc = 0
    prefix = [0]*n
    for i in range(n):
        prefix[i] = acc
        acc += nums[i]
        
    return prefix
print(prefixSum([1, 2, 3, 1]))