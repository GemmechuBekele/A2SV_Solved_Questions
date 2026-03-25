n = int(input())
nums = []
def printNum(n):
    if n == 0:
        return 
    nums.append(n)
    printNum(n-1)
printNum(n)

nums.sort()
for i in nums:
    print(i)

