
def findDuplicates(nums):
    integer_appearance = {}

    for num in nums:
        if num not in integer_appearance:
            integer_appearance[num] = 1
        else:
            integer_appearance[num] += 1

    duplicate = []
    for num, count in integer_appearance.items():
        if count == 2:
            duplicate.append(num)
    
    return sorted(duplicate)

numb = findDuplicates([4,3,2,7,8,2,3,1])
print(numb)