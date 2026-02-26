n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

le_step = 0
ri_step = 0
pos = [0]*(n+1) 

for i in range(n):
    pos[a[i]] = i+1

for j in b:
    le_step += pos[j]
    ri_step += n-pos[j]+1


print(le_step, ri_step)