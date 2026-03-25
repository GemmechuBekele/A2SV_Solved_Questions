def pivotIndex(nums):
    prefix = [0]*len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i] 
    
    index = -1
    total = prefix[len(nums)-1]
    for i in range(len(nums)):
        if i == 0:
            left_sum = 0
        else:
            left_sum = prefix[i-1]
        
        right_sum = total - prefix[i]
        
        if left_sum == right_sum:
            return i
    
    return index
pivot_index = pivotIndex([1,7,3,6,5,6])
print(pivot_index)