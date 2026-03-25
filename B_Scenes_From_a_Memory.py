t = int(input())

for _ in range(t):
    k = int(input())
    nums = input()
    found = False
    for ch in nums:
        if ch == "1" or ch == "4" or ch == "6" or ch == "9":
            print(1)
            print(ch)
            found = True
            break
    if found:
        continue
    
    left = 0
    for right in range(right+1, k):