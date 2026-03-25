n = int(input())
path = []
result = []
def backtrack():
    if len(path) == n:
        result.append(path.copy())
        return
    
    for i in range(1, n+1):
        if i not in path:
            path.append(i)
            backtrack()
            path.pop()

backtrack()
for i in result:
    print(*i)