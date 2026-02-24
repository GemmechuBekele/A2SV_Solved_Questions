n = int(input())
s = input()
count = 0

for i in range(n-1):
    for j in range(i+1, n):
        if s[i] == s[j]:
            count += 1
            break
        else:
            break
print(count)
