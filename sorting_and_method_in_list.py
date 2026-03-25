# nums = [2, 3, 9, 8, 5, 6, 4, 7]
# nums.sort(reverse=True)
# print(nums)
# sorted_list = sorted(nums, reverse=True)
# print(sorted_list)
# nums = [1, -6, -2, 0, -8]
# sorted_list = sorted(nums, key=abs)
# print(sorted_list)
# nums = [1, 2, 3, 5]
# # Finding missing number
# for i in range(1, 6):
#     if i not in nums:
#         print(i)

# a = [1,3,5]
# b = [2,4,5]
# for x in a:
#     if x in b:
#         print("common num:", x)

# Largest difference   
# words = ["apple","kiwi","banana"]
# # wordsLen = []
# # for i in words:
# #     wordsLen.append(len(i))

# # wordsLen.sort()
# # print(wordsLen[-1])
# print(sorted(words, key=len))
# what is wrong?
# nums = [7,1,5,3]
# maxdiff = float("-inf")
# # nums.sort()
# # print(nums[-1]-nums[0])
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         diff = abs(nums[i]-nums[j])
#         maxdiff = max(maxdiff, diff)

# print(maxdiff)

#Comprehension
# nums = [1, 2, 5, 7]

# seven = [num for num in nums if num==7]
# print(seven[-1])
# my_list = [[0]] * 5
# my_list[0][0] = 1 
# print(my_list)
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# green = "apple"
# green = "banana"
# green = "cherry"
# #unpacking tuple
# fruits = ("apple", "banana", "cherry", "oranges", "pineapples")
# green, yellow, *red = fruits  
# green = "apple"
# yellow = "banana"
# red = ["cherry", "oranges", "pineapples"]

a, b, c, n = map(int, input().split())
print([[x,y,z] for x in range(a+1) for y in range(b+1) for z in range(c+1) if x+y+z != n])