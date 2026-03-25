import sys
sys.setrecursionlimit(10**7)

n = int(input())
arr = list(map(int, input().split()))
arr = arr[:n]
def summation(arr, idx=0):
    if idx >= len(arr):
        return 0
    else:
        return arr[idx] + summation(arr, idx+1)

print(summation(arr))