def findDuplicates(nums):
    integer_appearance = {}

    for num in nums:
        if num not in integer_appearance:
            integer_appearance[num] = 1
        else:
            integer_appearance[num] += 1
    
    duplicates = []

    for twice, num in integer_appearance.items(): #[(4, 1), (3, 2), (2, 2), (7, 1), (8, 1), (1, 1)]
        if num == 2:
            duplicates.append(twice)
    
    return duplicates

numbers = findDuplicates([4,3,1,7,8,2,3,2])
