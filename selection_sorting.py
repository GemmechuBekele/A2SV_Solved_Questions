## [1, 3, 5, 4, 8, 6, 7]
def ss(arr):

    n = len(arr)
    #let minIndex = 0
    # minIndex = 0
    maxIndex = n-1

    for i in range(n):
        for j in range(n-i-1):
            # if arr[j] < arr[minIndex]:
            if arr[j] < arr[maxIndex]:
                # arr[j], arr[minIndex] = arr[minIndex], arr[j] 
                arr[j], arr[maxIndex] = arr[maxIndex], arr[j] 
                # minIndex = j
                maxIndex = j

    return arr

a = ss([1, 3, 5, 4, 8, 6, 7])
print(a)
