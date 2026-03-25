n = int(input())
nums = list(map(int, input().split()))
evenIndiceNums = []
def printNums(n, idx=0):
    if idx == len(nums):
        return
    if idx % 2 == 0:
        evenIndiceNums.append(nums[idx])
    printNums(n, idx+1)
printNums(nums)    

evenIndiceNums.reverse()
for i in evenIndiceNums:
    print(i, end=" ")