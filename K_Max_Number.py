n = int(input())
arr = list(map(int, input().split()))

def maxNumber(arr):
    if len(arr) == 1:
        return arr[0]
    maxNum = maxNumber(arr[1:])
    if arr[0] > maxNum:
        return arr[0]
    else:
        return maxNum
    
print(maxNumber(arr))
