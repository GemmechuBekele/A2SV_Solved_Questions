n = int(input())
k = int(input())
p = []
for _ in range(k):
    a, b = map(int, input().split())
    p.append((a, b))

result = []
path = []
used = set()

before = {i: [] for i in range(1, n+1)}

for a, b in p:
    before[b].append(a)

def backtrack():
    if len(path) == n:
        result.append(path.copy())
        return
    
    for num in range(1, n+1):
        if num in used:
            continue
        valid = True
        for pre in before[num]:
            if pre not in used:
                valid = False
                break
        if not valid:
            continue
        path.append(num)
        used.add(num)
        backtrack()

        path.pop()
        used.remove(num)

backtrack()

for perm in result:
    print(*perm)

print(len(result))