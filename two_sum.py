def twoSum(nums, target):
    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == target:
            index = [i, i+1]
    return index
print(twoSum([3,3], 6))