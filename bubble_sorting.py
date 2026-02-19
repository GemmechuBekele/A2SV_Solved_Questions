# [1, 3, 5, 4, 8, 6, 7]
def bs(arr):
    
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

a = bs([1, 3, 5, 4, 8, 6, 7])
print(a)